/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './base.css',
    './bro_website/static/**/*.{css,js}',
    './bro_website/templates/**/*.html',
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
          "primary": "#00daaa",
          "secondary": "#ff4000",
          "accent": "#007bc7",
          "neutral": "#141a18",
          "base-100": "#f3ffeb",
          "info": "#00ddff",
          "success": "#00c47f",
          "warning": "#f39e00",
          "error": "#e32535",
        },
      },
      {
        'dark': {
          "primary": "#ccff00",
          "secondary": "#ff4000",
          "accent": "#007bc7",
          "neutral": "#0e0f11",
          "base-100": "#0e0f11",
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

