/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "base.css",
    "bro/**/static/**/*.{css,js}",
    "bro/**/templates/**/*.html",
    "static/**/*.{css,js}",
    "templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: (theme) => ({
        sans: ['Figtree']
      }),
      typography: (theme) => ({
        DEFAULT: {
          css: {
            h1: {
              fontWeight: '300',
            },
            h2: {
              fontWeight: '300',
            },
            h3: {
              fontWeight: '400',
            },
            h4: {
              fontWeight: '400',
            },
            h5: {
              fontWeight: '500',
            },
            h6: {
              fontWeight: '500',
            }
          }
        }
      }),
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("daisyui")
  ],
  daisyui: {
    themes: [
      {
        light: {
          "primary": "#4CAF50", // Green
          "secondary": "#8BC34A", // Light Green
          "accent": "#FFF7ED", // Lime
          "neutral": "#F5F5F5", // Light Gray
          "base-100": "#FFFFFF", // White
          "info": "#2196F3", // Blue
          "success": "#4CAF50", // Green
          "warning": "#FF9800", // Orange
          "error": "#F44336", // Red
          "--rounded-btn": "100rem"
        }
      },
      {
        dark: {
          "primary": "#4CAF50", // Green
          "secondary": "#8BC34A", // Light Green
          "accent": "#FFF7ED", // Lime
          "neutral": "#454545", // Light Gray
          "base-100": "#222222", // White
          "info": "#2196F3", // Blue
          "success": "#4CAF50", // Green
          "warning": "#FF9800", // Orange
          "error": "#F44336", // Red
          "--rounded-btn": "100rem"
        }
      }
    ],
    darkTheme: 'light'
  }
}