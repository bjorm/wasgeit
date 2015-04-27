var React = require('react');
var WasGeit = require('./components/WasGeit.react');

require('./style/css/bootstrap.min.css');
require('./style/style.less');
require('file?name=index.html!./index.html');

React.render(<WasGeit />, document.getElementById("wasgeit"));
