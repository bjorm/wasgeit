var React = require('react');
var restful = require('restful.js');
var _ = require('lodash');

var api = restful('localhost:8080');

var Agenda = React.createClass({
    getInitialState: function() {
        return { events: {} }
    },
    componentDidMount: function() {
        api.all('rest/agenda').getAll().then(function(response) {
            if (this.isMounted()) {
                this.setState({
                    events: response.body().data()
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
