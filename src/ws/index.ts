import { Hono } from 'hono';
import appWsRealTimeCursors from './real-time-cursors/route';

const appWs = new Hono();

appWs.route('/realtime-cursors', appWsRealTimeCursors);

export default appWs;
