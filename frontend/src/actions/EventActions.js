import Backend from './Backend';
import AppDispatcher from '../dispatcher/Dispatcher';
import Actions from './Actions';

class EventActions {
    loadEvents() {
        Backend.all('agenda').getAll().then((response) => {
            AppDispatcher.dispatch({ actionType: Actions.EVENTS_LOADED, events: response.body(false) });
        });
    }
}

export default new EventActions();