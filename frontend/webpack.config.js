module.exports = {
    entry: './src/index.js',
    output: {
        path: __dirname + '/src',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.css$/, loader: 'style!css' },
            { test: /\.jsx$/, loader: 'jsx-loader?harmony' },
            { test: /\.es6/, loader: 'babel-loader' }
        ]
    },
    resolve: {
        // Allow require('./blah') to require blah.jsx
        extensions: ['', '.js', '.jsx', '.es6']
    },
    devServer: {
        proxy: {
            '/rest/*': 'http://localhost:5000'
        }
    }
};
