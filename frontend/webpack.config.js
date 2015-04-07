module.exports = {
    entry: "./src/index.js",
    output: {
        path: __dirname + "/src",
        filename: "bundle.js"
    },
    module: {
        loaders: [
            { test: /\.css$/, loader: "style!css" },
            { test: /\.jsx$/, loader: 'jsx-loader?harmony' }
        ]
    },
    resolve: {
        // Allow require('./blah') to require blah.jsx
        extensions: ['', '.js', '.jsx']
    },
    devServer: {
        proxy: {
            '/rest/*': 'http://localhost:5000'
        }
    }
};