/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./clients/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
        mono: ['Courier Prime', 'monospace'],
      },
      colors: {
        accent: '#f5e642',
        ink: '#1a1a1a',
      }
    }
  },
  plugins: [],
}
