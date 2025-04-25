import { Hono } from 'hono';
import routeDevice from './connected-devices/route';

const appApi = new Hono();

appApi.route('/connected-devices', routeDevice);

export default appApi;
