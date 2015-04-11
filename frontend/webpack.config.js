var ExtractTextPlugin = require("extract-text-webpack-plugin");
module.exports = {
    entry: './src/index.react.js',
    output: {
        path: __dirname + '/src',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.less$/, loader: ExtractTextPlugin.extract("style-loader", "css-loader!less-loader") },
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
    },
    plugins: [
        new ExtractTextPlugin("style.css")
    ]
};
