module.exports = {
    entry: './src/index.react.js',
    output: {
        path: __dirname + '/src',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.less$/, loader: 'style!css!less' },
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
