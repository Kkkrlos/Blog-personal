/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/*.html',
    './**/templates/partials/*.html'
  ],
  theme: {
    extend: {
      screens: {
        '320x566': {'raw': '(width: 320px) and (height: 566px)'}
      }
    },
  },
  plugins: [],
}

