import React from 'react';
import VenueActions from '../actions/VenueActions';

export default class Venue extends React.Component {
    _onClick() {
        VenueActions.venueClicked(this.props.venue.name);
    }
    render() {
        return (<li onClick={this._onClick.bind(this)}>{this.props.venue.name}</li>);
    }
}