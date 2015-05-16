import Backend from './Backend';
import AppDispatcher from '../dispatcher/Dispatcher';
import Actions from './Actions';

class VenueActions {
    venueClicked(id) {
        AppDispatcher.dispatch({ actionType: Actions.VENUE_CLICKED, id });
    }

    loadVenues() {
        Backend.all('venues').getAll().then((response) => {
            AppDispatcher.dispatch({ actionType: Actions.VENUES_LOADED, venues: response.body(false) });
        });

    }

    showAllVenues() {
        AppDispatcher.dispatch({ actionType: Actions.VENUES_SHOW_ALL });
    }
}

export default new VenueActions();