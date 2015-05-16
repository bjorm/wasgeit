import AppDispatcher from '../dispatcher/Dispatcher';
import Actions from '../actions/Actions';
import _ from 'lodash';
import EventEmitter from 'events';

var venues = [];
var CHANGE_EVENT = 'change';

// TODO do not use class, it's a singleton
class VenueStore extends EventEmitter {
    constructor() {
        super();
    }

    getState() {
        return { venues };
    }

    getSelectedVenues() {
        return _.pluck(_.where(venues, { selected: true }), 'name');
    }

    areAllVenuesVisible() {
        return !_.find(venues, 'selected', false);
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

var venueStore = new VenueStore();

venueStore.dispatchToken = AppDispatcher.register(function(action) {
    // TODO refactor
    if (action.actionType === Actions.VENUE_CLICKED) {
        venues.forEach((venue) => { _.set(venue, 'selected', false) });
        var clickedVenue = _.find(venues, 'name', action.id);
        if (clickedVenue) {
            _.set(clickedVenue, 'selected', true);
            venueStore.emitChange();
        }
    } else if (action.actionType === Actions.VENUES_LOADED) {
        venues = action.venues.map((venue) => { return _.defaults(venue, { selected: true }); });
        venueStore.emitChange();
    } else if (action.actionType === Actions.VENUES_SHOW_ALL) {
        venues.forEach((venue) => { _.set(venue, 'selected', true) });
        venueStore.emitChange();
    }
});



export default venueStore;
