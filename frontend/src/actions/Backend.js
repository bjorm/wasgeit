import 'whatwg-fetch';
import restful, { fetchBackend } from 'restful.js';

const api = restful('http://' + location.host + '/rest', fetchBackend(fetch));
export default api;