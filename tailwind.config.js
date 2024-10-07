/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "base.css",
    "bro/**/models.py",
    "bro/**/static/**/*.{css,js}",
    "bro/**/templates/**/*.html",
    "static/**/*.{css,js}",
    "templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: (def) => ({
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
        "light": {
          "primary": "#8BC34A", // Green
          "secondary": "#C3644A", // Light Green
          "accent": "#FFE4C4", // Lime
          "neutral": "#EFEFE0", // Light Gray
          "base-100": "#FFFFFF", // White
          "info": "#2196F3", // Blue
          "success": "#4CAF50", // Green
          "warning": "#FF9800", // Orange
          "error": "#F44336", // Red
          "--rounded-box": "0.5rem",
          "--rounded-btn": "100rem",
          "--rounded-badge": "100rem"
        }
      },
      {
        "dark": {
          "primary": "#8BC34A", // Green
          "secondary": "#C3644A", // Light Green
          "accent": "#FFE4C4", // Lime
          "neutral": "#EFEFE0", // Dark Gray
          "base-100": "#FFFFFF", // Neutral Blackish
          "info": "#2196F3", // Blue
          "success": "#4CAF50", // Green
          "warning": "#FF9800", // Orange
          "error": "#F44336", // Red
          "--rounded-box": "0.5rem",
          "--rounded-btn": "100rem",
          "--rounded-badge": "100rem"
        }
      }
    ],
    darkTheme: 'dark'
  }
}