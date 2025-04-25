import { DurableObject } from 'cloudflare:workers';
import { ENV_REALTIME_CURSORS } from './types';
import { SessionHandler } from './SessionHandler';

export class RealTimeCursors extends DurableObject {
  state: DurableObjectState;
  env: ENV_REALTIME_CURSORS;

  constructor(state: DurableObjectState, env: ENV_REALTIME_CURSORS) {
    super(state, env);
    this.state = state;
    this.env = env;
  }

  async fetch(req: Request) {
    if (req.headers.get('Upgrade') !== 'websocket') {
      return new Response('Expected WebSocket', { status: 426 });
    }
    const country = req.headers.get('cf-ipcountry') || 'XX';

    const [client, ws] = Object.values(new WebSocketPair());
    const sessionHandler = new SessionHandler();
    sessionHandler.handle(ws, country);

    return new Response(null, { status: 101, webSocket: client });
  }
}
