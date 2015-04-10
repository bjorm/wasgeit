var React = require('react');
var _ = require('lodash');

var Event = React.createClass({
    render: function() {
        var event = this.props.event;
        return (<li>{event.venue}: <a href={event.link}>{event.title}</a></li>);
    }
});

module.exports = Event;