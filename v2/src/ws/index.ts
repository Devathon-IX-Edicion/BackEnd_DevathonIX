import { Hono } from 'hono';
import wsHandler from './devathon/route';

const appWs = new Hono();

appWs.route('/realtime-devathon', wsHandler);

export default appWs;
