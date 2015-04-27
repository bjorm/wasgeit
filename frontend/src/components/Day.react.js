var React = require('react');
var _ = require('lodash');

var Event = require('./Event.react');

var Day = React.createClass({
    render: function() {
        var events = [];
        this.props.events.forEach(function(event) {
            events.push(<Event key={event.link} event={event}/>)
        });
        return (
            <li>
                <h2>
                    <time date="{this.props.date}">{this.props.date}</time>
                </h2>
                <ul className={'list-unstyled'}>{events}</ul>
            </li>
        );
    }
});

module.exports = Day;