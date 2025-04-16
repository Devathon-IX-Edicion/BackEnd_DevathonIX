import { Hono } from 'hono';
import { upgradeWebSocket } from 'hono/cloudflare-workers';

const wsRoute = new Hono();

wsRoute.get(
  '/',
  upgradeWebSocket((c) => {
    return {
      onMessage(event, ws) {
        console.log(`Message from client: ${event.data}`, c.req);
        ws.send('Hello from server!');
      },
      onClose: () => {
        console.log('Connection closed');
      },
    };
  }),
);

export default wsRoute;
