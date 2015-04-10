import AppDispatcher from '../dispatcher/Dispatcher';
import Actions from '../actions/Actions';
import _ from 'lodash';
import EventEmitter from 'events';
import VenueStore from './VenueStore';

var CHANGE_EVENT = 'change';

var allEvents = {};
var visibleEvents = {};

class EventStore extends EventEmitter {
    constructor() {
        super();
    }

    getState() {
        return { events: visibleEvents };
    }

    emitChange() {
        this.emit(CHANGE_EVENT);
    }

    addChangeListener(callback) {
        this.on(CHANGE_EVENT, callback);
    }

    removeChangeListener(callback) {
        this.removeListener(CHANGE_EVENT, callback);
    }
}

var eventStore = new EventStore();

function filterEvents() {
    var selectedVenues = VenueStore.getSelectedVenues();

    return _.reduce(allEvents, (result, events, date) => {
        var filteredEvents = _.filter(events, (event) => {
            return _.contains(selectedVenues, event.venue);
        });
        if (filteredEvents.length > 0) {
            result[date] = filteredEvents;
        }
        return result;
    }, {});
}

AppDispatcher.register(function(action) {
    if (action.actionType === Actions.VENUE_CLICKED) {
        AppDispatcher.waitFor([VenueStore.dispatchToken]);
        visibleEvents = filterEvents();
        eventStore.emitChange();
    } else if (action.actionType === Actions.EVENTS_LOADED) {
        allEvents = action.events;
        visibleEvents = filterEvents();
        eventStore.emitChange();
    }
});

export default eventStore;