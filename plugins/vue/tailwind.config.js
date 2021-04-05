const colors = require('tailwindcss/colors');

module.exports = {
    purge: {content: ['./public/**/*.html', './src/**/*.vue']},
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {colors},
        extend: {
            colors: {
                caldera: {
                    // red: '#C31135'
                    red: '#750b20',
                    reddish: '#AA324A',
                    // green: '#21770D', // the real green
                    green: '#750b20',
                    brown: '#755F63',
                    grayish: '#151515',

                }
            },
            fontFamily: {

            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
