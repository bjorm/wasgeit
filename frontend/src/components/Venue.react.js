import React from 'react';
import VenueActions from '../actions/VenueActions';

export default class Venue extends React.Component {
    _onClick() {
        VenueActions.venueClicked(this.props.venue.name);
    }
    render() {
        var style = this.props.venue.selected ? 'active' : '';
        return (
            <li className={style + ' fat'} onClick={this._onClick.bind(this)}>
                <a href="#">{this.props.venue.name}</a>
            </li>
        );
    }
}