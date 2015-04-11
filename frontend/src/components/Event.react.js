var React = require('react');
var _ = require('lodash');

var Event = React.createClass({
    render: function() {
        var event = this.props.event;
        return (
            <li>
                <span className={'ink-label grey'}>{event.venue}</span>
                &nbsp;
                <a href={event.link}>{event.title}</a>
            </li>
        );
    }
});

module.exports = Event;