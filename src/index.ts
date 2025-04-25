import { Hono } from 'hono';
import appApi from './api';
/* [start] WebSockets */
import appWs from './ws';
export { RealTimeCursors as MyDurableObject } from './ws/real-time-cursors/RealTimeCursos';
/* [end] WebSockets */

const app = new Hono();

app.route('/api', appApi);
app.route('/ws', appWs);

export default app;
