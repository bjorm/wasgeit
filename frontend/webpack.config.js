module.exports = {
    entry: './src/index.react.js',
    output: {
        path: __dirname + '/src',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.css$/, loader: 'style!css' },
            { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' }
        ]
    },
    resolve: {
        extensions: ['', '.js']
    },
    devServer: {
        proxy: {
            '/rest/*': 'http://localhost:5000'
        }
    }
};
