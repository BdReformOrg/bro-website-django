/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './base.css',
    './bro_website/static/**/*.{css,js}',
    './bro_website/templates/**/*.html',
    './bro_frontend/static/**/*.{css,js}',
    './bro_frontend/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['Bitter', 'ui-serif', 'Georgia', 'Cambria', "Times New Roman", 'Times', 'serif'],
        sans: ['Raleway', 'ui-sans-serif', 'system-ui', 'sans-serif', "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"]
      }
    },
  },
  plugins: [
    require('daisyui')
  ],
  daisyui: {
    themes: [
      {
        'light': {
          "primary": "#778e61",
          "secondary": "#ab3131",
          "accent": "#ede0a6",
          "neutral": "#f1f4ef",
          "base-100": "#f6f0d3",
          "info": "#00ddff",
          "success": "#00c47f",
          "warning": "#f39e00",
          "error": "#e32535",
        },
      },
      {
        'dark': {
          "primary": "#507b58",
          "secondary": "#540502",
          "accent": "#ede0a6",
          "neutral": "#3c4731",
          "base-100": "#0c0e0a",
          "info": "#00ddff",
          "success": "#00c47f",
          "warning": "#f39e00",
          "error": "#e32535",
        },
      }
    ],
    darkTheme: 'dark'
  }
}

