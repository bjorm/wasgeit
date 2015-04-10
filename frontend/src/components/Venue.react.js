import React from 'react';

export default class Venue extends React.Component {
    render() {
        return (<li>{this.props.venue.name}</li>);
    }
}