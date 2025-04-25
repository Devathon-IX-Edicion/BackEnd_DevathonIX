import { DurableObject } from 'cloudflare:workers';
import { ENV_DEVATHON } from '.';
import { ConnecHandler } from './ConnecHandler';

export class modelDB extends DurableObject {
  state: DurableObjectState;
  env: ENV_DEVATHON;

  constructor(state: DurableObjectState, env: ENV_DEVATHON) {
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
    const sessionHandler = new ConnecHandler();
    sessionHandler.handle(ws, country);

    return new Response(null, { status: 101, webSocket: client });
  }
}
