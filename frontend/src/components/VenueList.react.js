var React = require('react');
var VenueStore = require('../stores/VenueStore');
var Venue = require('./Venue.react');

var VenueList = React.createClass({
    getInitialState: function() {
        return { venues: [] };
    },
    componentDidMount: function() {
        VenueStore.getAll().then(function(venues) {
            if (this.isMounted()) {
                this.setState({ venues: venues});
            }
        }.bind(this));
    },
    render: function() {
        var venues = [];
        this.state.venues.forEach((venue) => {
            venues.push(<Venue venue={venue} />);
        });
        return (<div>Select venues: <ul>{venues}</ul></div>);
    }
});

module.exports = VenueList;