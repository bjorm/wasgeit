var React = require('react');
var _ = require('lodash');
var moment = require('moment');
var Event = require('./Event.react');

var Day = React.createClass({
    render: function() {
        var events = [];
        this.props.events.forEach(function(event) {
            events.push(<Event key={event.link} event={event}/>)
        });
        let date = moment(this.props.date, "YYYY-MM-DD").format("ddd, DD. MMM");
        return (
            <li>
                <h2>
                    <time date="{this.props.date}">{date}</time>
                </h2>
                <ul className={'list-unstyled'}>{events}</ul>
            </li>
        );
    }
});

module.exports = Day;