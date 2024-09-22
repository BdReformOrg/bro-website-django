/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './base.css',
    './bro/**/models.py',
    './bro/**/templates/**/*.html',
    './bro/**/static/**/*.{css,js}',
    './templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Figtree', 'ui-sans-serif', 'system-ui', 'sans-serif', "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"]
      }
    },
  },
  plugins: [
    require('daisyui')
  ],
  daisyui: {
    themes: [
      {
        light: {
          primary: '#507B58',
          secondary: '#AB3131',
          accent: '#EDE0A6',
          neutral: '#F7EAEA',
          'base-100': '#ffffff',
          info: '#00ddff',
          success: '#00c47f',
          warning: '#f39e00',
          error: '#e32535',
          '--rounded-btn': '9999rem',
        },
      },
      {
        dark: {
          primary: '#094a25',
          secondary: '#bc2023',
          accent: '#f8b324',
          neutral: '#134e4a',
          'base-100': '#032b2a',
          info: '#00ddff',
          success: '#00c47f',
          warning: '#f39e00',
          error: '#e32535',
          '--rounded-btn': '9999rem',
        },
      },
    ],
    darkTheme: 'dark'
  }
}

// themes: [
//   {
//     'light': {
//       "primary": "#bef264",
//       "secondary": "#0d9488",
//       "accent": "#022c22",
//       "neutral": "#fff7ed",
//       "base-100": "#ffffff",
//       "info": "#00ddff",
//       "success": "#00c47f",
//       "warning": "#f39e00",
//       "error": "#e32535",
//       "--rounded-btn": "9999rem",
//     },
//   },
//   {
//     'dark': {
//       "primary": "#507b58",
//       "secondary": "#540502",
//       "accent": "#ede0a6",
//       "neutral": "#3c4731",
//       "base-100": "#0c0e0a",
//       "info": "#00ddff",
//       "success": "#00c47f",
//       "warning": "#f39e00",
//       "error": "#e32535",
//     },
//   }
// ],