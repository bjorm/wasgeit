import React from 'react';
import _ from 'lodash';
import VenueStore from '../stores/VenueStore';
import VenueActions from '../actions/VenueActions';

var Event = React.createClass({
    getInitialState: function() {
        return this._getState();
    },
    componentDidMount: function() {
        VenueStore.addChangeListener(this._onChange);
    },
    componentWillUnmount: function() {
        VenueStore.removeChangeListener(this._onChange);
    },
    render: function() {
        var classes = ['btn', 'btn-default', 'btn-show-all'];
        if (this.state.hidden) {
            classes.push('hidden')
        }
        return (
            <button className={classes.join(' ')} onClick={this._onClick}>Alle anzeigen</button>
        );
    },
    _onClick: function() {
        VenueActions.showAllVenues();
    },
    _onChange: function() {
        this.setState(this._getState());
    },
    _getState: () => {
        return { hidden: VenueStore.areAllVenuesVisible() };
    }
});

export default Event;