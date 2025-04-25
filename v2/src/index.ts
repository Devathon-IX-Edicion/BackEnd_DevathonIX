import { Hono } from 'hono';
import appWs from './ws';
export { modelDB } from './ws/devathon/realtime-app';
const app = new Hono();
app.route('/ws', appWs);
export default app;
