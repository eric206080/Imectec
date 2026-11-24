/** Paleta basada en el logo de IMECTEC (engranaje azul + rayo amarillo) */
module.exports = {
  content: ['./*.html', './*/index.html', './js/*.js', './tools/*.py'],
  theme: {
    extend: {
      colors: {
        // Azul del engranaje
        primary: {
          50: '#eef1fb', 100: '#dbe1f5', 200: '#b9c4eb', 300: '#8c9fdc', 400: '#5f78c8',
          500: '#3f5ab3', 600: '#33479a', 700: '#2e407a', 800: '#252b66', 900: '#1a1f4d', 950: '#0f1233'
        },
        // Amarillo / ámbar del rayo
        accent: {
          50: '#fffbea', 100: '#fff3c4', 200: '#ffe78a', 300: '#ffe030', 400: '#fdd023',
          500: '#ffb101', 600: '#e08e00', 700: '#b86b00', 800: '#8f5207', 900: '#74430b'
        },
        navy: { DEFAULT: '#252b66', dark: '#0f1233' }
      },
      fontFamily: {
        heading: ['Outfit', 'system-ui', 'sans-serif'],
        body: ['"DM Sans"', 'system-ui', 'sans-serif'],
        brand: ['Outfit', 'system-ui', 'sans-serif']
      },
      keyframes: {
        float: { '0%, 100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(-14px)' } },
        fadeUp: { from: { opacity: '0', transform: 'translateY(24px)' }, to: { opacity: '1', transform: 'translateY(0)' } }
      },
      animation: {
        float: 'float 7s ease-in-out infinite',
        'fade-up': 'fadeUp .9s ease-out both'
      }
    }
  },
  plugins: []
};
