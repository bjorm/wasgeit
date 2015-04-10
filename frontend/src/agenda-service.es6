import restful from 'restful.js';

var api = restful('localhost:8080');

export function getAll() {
    return api.all('rest/agenda').getAll().then(function(response) {
        return response.body().data()
    });
}