import { Hono } from 'hono';
import { ENV_DEVATHON } from '.';

const appWsRealTimeCursors = new Hono<{ Bindings: ENV_DEVATHON }>();

appWsRealTimeCursors.get('/', async (c) => {
  const id = c.env.DEVATHON.idFromName('REALTIME_EVATHON');
  const obj = c.env.DEVATHON.get(id);
  return await obj.fetch(c.req.raw);
});

export default appWsRealTimeCursors;
