var React = require('react');
var _ = require('lodash');
var agendaService = require('./agenda-service');

var Agenda = React.createClass({
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

var Event = React.createClass({
    render: function() {
        var event = this.props.event;
        return (<li>{event.venue}: <a href={event.link}>{event.title}</a></li>);
    }
});

var Day = React.createClass({
    render: function() {
        var events = [];
        this.props.events.forEach(function(event) {
            events.push(<Event event={event}/>)
        });
        return (
            <li>
                <time date="{this.props.date}">{this.props.date}</time>
                <ul>{events}</ul>
            </li>
        );
    }
});

React.render(<Agenda/>, document.getElementById("agenda"));
