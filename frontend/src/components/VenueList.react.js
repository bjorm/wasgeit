import React from 'react';
import VenueStore from '../stores/VenueStore';
import Venue from './Venue.react';
import VenueActions from '../actions/VenueActions';

var VenueList = React.createClass({
    getInitialState: function() {
        return VenueStore.getState();
    },
    componentDidMount: function() {
        VenueStore.addChangeListener(this._onChange);
        VenueActions.loadVenues();
    },
    componentWillUnmount: function() {
        VenueStore.removeChangeListener(this._onChange);
    },
    render: function() {
        var venues = [];
        this.state.venues.forEach((venue) => {
            venues.push(<Venue key={venue.id} venue={venue} />);
        });
        return <ul className={'nav nav-pills'}>{venues}</ul>;
    },
    _onChange: function() {
        this.setState(VenueStore.getState());
    }
});

export default VenueList;