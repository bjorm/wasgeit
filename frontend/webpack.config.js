var ExtractTextPlugin = require('extract-text-webpack-plugin');
var webpack = require('webpack');
require('es6-promise').polyfill();

module.exports = {
    entry: './src/index.react.js',
    output: {
        path: __dirname + '/target',
        filename: 'bundle.min.js'
    },
    module: {
        loaders: [
            {test: /\.less$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader!less-loader')},
            {test: /\.css$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader!')},
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "url-loader?limit=10000&minetype=application/font-woff"
            },
            {test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader"},
            {test: /\.js$/, exclude: /node_modules/, loader: 'babel', query: { presets: ['react', 'es2015'] } }
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
        new ExtractTextPlugin("style.css"),
        new webpack.optimize.UglifyJsPlugin()
    ]
};
