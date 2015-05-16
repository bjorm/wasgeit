var React = require('react');

var VenueList = require('./VenueList.react');
var Agenda = require('./Agenda.react');
var ShowAll = require('./ShowAll.react');

var WasGeit = React.createClass({
    render: function() {
        return (<div><ShowAll /><VenueList /><Agenda /></div>);
    }
});

module.exports = WasGeit;