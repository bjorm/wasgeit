import Backend from './Backend'

export function getAll() {
    return Backend.all('agenda').getAll().then((response) => { return response.body().data() });
}

