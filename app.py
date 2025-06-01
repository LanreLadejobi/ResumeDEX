from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import openai

load_dotenv()

app = Flask(__name__)

# Tell openai-python to route to OpenRouter
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"
openai.organization = "openrouter"  # Required by OpenRouter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    job_title = request.form.get('job_title')
    experience = request.form.get('experience')

    if not job_title or not experience:
        return "Missing job title or experience", 400

    prompt = (
        f"Write 2 strong, ATS-friendly resume bullet points for a student who worked as a {job_title}. "
        f"They had this experience: {experience}. Use action verbs and quantify results where possible."
    )

    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",  # Required format for OpenRouter
            messages=[{"role": "user", "content": prompt}]
        )
        ai_output = response.choices[0].message.content
    except Exception as e:
        ai_output = f"Error generating content:\n\n{e}"

    return render_template('result.html', output=ai_output)

if __name__ == "__main__":
    app.run(debug=True)
