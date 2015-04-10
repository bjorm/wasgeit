import Backend from './Backend'

export function getAll() {
    return Backend.all('venues').getAll().then((response) => { return response.body(false); });
}
