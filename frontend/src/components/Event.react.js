import React from 'react';
import _ from 'lodash';

var Event = React.createClass({
    render: function() {
        var event = this.props.event;
        return (
            <li>
                <span className={'label label-default'}>{event.venue}</span>
                &nbsp;
                <a href={event.link} rel="external">{event.title}</a>
            </li>
        );
    }
});

export default Event;