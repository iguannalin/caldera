const colors = require('tailwindcss/colors');

module.exports = {
    purge: {content: ['./public/**/*.html', './src/**/*.vue']},
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {colors},
        extend: {
            colors: {
                caldera: {
                    red: '#750b20'
                }
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
