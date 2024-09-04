/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mytheme: {
          // https://daisyui.com/theme-generator/
          "primary": "#ff00ff",
          "secondary": "#ff00ff",
          "accent": "#00ffff",
          "neutral": "#ff00ff",
          "base-100": "#111827",
          "info": "#0000ff",
          "success": "#22c55e",
          "warning": "#fde047",
          "error": "#ff0000",
        }
      }
    ]
  },
  plugins: [
    require('daisyui'),
  ],
}

