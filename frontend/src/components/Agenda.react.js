var React = require('react');
var _ = require('lodash');

var EventStore = require('../stores/EventStore');
var EventActions = require('../actions/EventActions');
var Day = require('./Day.react');

var Agenda = React.createClass({
    getInitialState: function() {
        return EventStore.getState();
    },
    componentDidMount: function() {
        EventStore.addChangeListener(this.onChange);
        EventActions.loadEvents();
    },
    componentWillUnmount: () => {
        EventStore.removeChangeListener(this.onChange);
    },
    render: function() {
        var days = [];
        _.forOwn(this.state.events, function(events, date) {
            days.push(<Day date={date} events={events} />);
        });
        return (<ol className={'list-unstyled'}>{days}</ol>);
    },
    onChange: function() {
        this.setState(EventStore.getState());
    }
});

module.exports = Agenda;