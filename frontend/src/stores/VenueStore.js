import AppDispatcher from '../dispatcher/Dispatcher';
import Actions from '../actions/Actions';
import _ from 'lodash';
import EventEmitter from 'events';

var venues = [];
var selectedVenueIds = [];
var CHANGE_EVENT = 'change';

class VenueStore extends EventEmitter {
    constructor() {
        super();
    }

    getState() {
        return { venues };
    }

    getSelectedVenues() {
        return selectedVenueIds;
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

    if (action.actionType === Actions.VENUE_CLICKED) {
        if (_.includes(selectedVenueIds, action.id)) {
            selectedVenueIds = _.without(selectedVenueIds, action.id);
        } else {
            selectedVenueIds.push(action.id);
        }
        venueStore.emitChange();
    } else if (action.actionType === Actions.VENUES_LOADED) {
        venues = action.venues;
        selectedVenueIds = _.pluck(venues, 'name');
        console.log(selectedVenueIds);
        venueStore.emitChange();
    }
});



export default venueStore;
