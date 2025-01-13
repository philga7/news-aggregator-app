/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {
      fontFamily: {
        mono: ['Roboto Mono', 'monospace'],
      },
      colors: {
        'custom-bg': '#000000',
        'custom-text': '#FFFFFF',
        primary: '#000000',
        secondary: '#ffffff',
        accent: '#808080', // grayscale for accents
      },
    },
  },
  daisyui: {
    themes: [
      {
        brutalist: {
          primary: '#000000',
          secondary: '#ffffff',
          accent: '#808080',
          neutral: '#f5f5f5',
          'base-100': '#ffffff',
          info: '#000000',
          success: '#000000',
          warning: '#000000',
          error: '#000000',
        },
      },
    ],
  },
  plugins: [
    require('daisyui'),
  ],
};

