/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#1A2A4F",      // navy blue
          light: "#3C4F76",
          dark: "#111A33"
        },
        accent: "#D3E0EA",         // light blue-gray
      },
      fontFamily: {
        sans: ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
      }
    }
  },
  plugins: [],
}
