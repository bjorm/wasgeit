var React = require('react');

var VenueList = require('./VenueList.react');
var Agenda = require('./Agenda.react');

var WasGeit = React.createClass({
    render: function() {
        return (<div><VenueList /><Agenda /></div>);
    }
});

module.exports = WasGeit;