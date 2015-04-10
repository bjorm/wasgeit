var React = require('react');
var _ = require('lodash');
var agendaService = require('../stores/EventStore');
var Day = require('./Day.react');

var Days = React.createClass({
    getInitialState: function() {
        return { events: {} }
    },
    componentDidMount: function() {
        agendaService.getAll().then(function(events) {
            if (this.isMounted()) {
                this.setState({
                    events: events
                });
            }
        }.bind(this));
    },
    render: function() {
        var days = [];
        _.forOwn(this.state.events, function(events, date) {
            days.push(<Day date={date} events={events} />);
        });
        return (<ol>{days}</ol>);
    }
});

//module.exports = Days;