import { Hono } from 'hono';
import { ENV_REALTIME_CURSORS } from './types';

const appWsRealTimeCursors = new Hono<{ Bindings: ENV_REALTIME_CURSORS }>();

appWsRealTimeCursors.get('/', async (c) => {
  const id = c.env.REALTIME_CURSORS.idFromName('realtime-cursors');
  const obj = c.env.REALTIME_CURSORS.get(id);
  return await obj.fetch(c.req.raw);
});

export default appWsRealTimeCursors;
