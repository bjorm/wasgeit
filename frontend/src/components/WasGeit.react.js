import React from 'react';

import VenueList from './VenueList.react';
import Agenda from './Agenda.react';
import ShowAll from './ShowAll.react';

var WasGeit = React.createClass({
    render: function() {
        return (<div><ShowAll /><VenueList /><Agenda /></div>);
    }
});

export default WasGeit;