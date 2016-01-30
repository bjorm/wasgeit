import React from 'react';
import _ from 'lodash';

import EventStore from '../stores/EventStore';
import EventActions from '../actions/EventActions';
import Day from './Day.react';

var Agenda = React.createClass({
    getInitialState: function () {
        return EventStore.getState();
    },
    componentDidMount: function () {
        EventStore.addChangeListener(this.onChange);
        EventActions.loadEvents();
    },
    componentWillUnmount: () => {
        EventStore.removeChangeListener(this.onChange);
    },
    render: function() {
        let days = [];
        _.forOwn(this.state.events, function(events, date) {
            days.push(<Day key={date} date={date} events={events} />);
        });
        return (<ol className={'list-unstyled'}>{_.sortBy(days, (day) => day.key)}</ol>);
    },
    onChange: function () {
        this.setState(EventStore.getState());
    }
});

export default Agenda;