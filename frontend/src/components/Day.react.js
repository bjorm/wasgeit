import React from 'react';
import _ from 'lodash';
import moment from 'moment';
import Event from './Event.react';

var Day = React.createClass({
    render: function() {
        return (
            <li>
                <h2>
                    <time date="{this.props.date}">
                        { moment(this.props.date, "YYYY-MM-DD").format("ddd, DD. MMM") }
                    </time>
                </h2>
                <ul className={'list-unstyled'}>
                    { this.props.events.map((event) => <Event key={event.link} event={event}/>) }
                </ul>
            </li>
        );
    }
});

export default Day;