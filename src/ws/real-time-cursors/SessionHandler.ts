import { generatePastelColor } from '~/src/utils/generatePastelColor';
import { CursorPosition, DeviceInfo, RealTimeCursorEvent } from './types';
import { WebSocketBroadcaster } from './WebSocketBroadcaster';

export class SessionHandler {
  private static connections: Record<string, WebSocket> = {};
  private static deviceInfo: Record<string, DeviceInfo> = {};
  private static cursors: Record<string, CursorPosition> = {};
  private broadcaster: WebSocketBroadcaster;
  private clientId: string;

  constructor() {
    this.clientId = crypto.randomUUID();
    this.broadcaster = new WebSocketBroadcaster(SessionHandler.connections, this.clientId);
  }

  handle(ws: WebSocket, region: string) {
    ws.accept();

    SessionHandler.connections[this.clientId] = ws;
    SessionHandler.deviceInfo[this.clientId] = { region, color: generatePastelColor() };

    this.broadcaster.send({
      type: 'device_connected',
      payload: {
        devices: SessionHandler.deviceInfo,
        id: this.clientId,
        cordsMause: SessionHandler.cursors,
      },
    });

    this.broadcaster.broadcastExcept({
      type: 'device_joined',
      payload: {
        [this.clientId]: SessionHandler.deviceInfo[this.clientId],
      },
    });

    ws.addEventListener('message', this.handlerMessage);
    ws.addEventListener('close', this.handlerClose);
    ws.addEventListener('error', this.handlerError);
  }

  private handlerMessage = (e: MessageEvent) => {
    try {
      const payload: RealTimeCursorEvent = JSON.parse(e.data.toString());
      switch (payload.type) {
        case 'cursor_moved': {
          const cursorPosition = payload.payload;
          SessionHandler.cursors[this.clientId] = cursorPosition[this.clientId];
          this.broadcaster.broadcastExcept({
            type: 'cursor_moved',
            payload: cursorPosition,
          });
          break;
        }
        default:
          console.error('Unknown message type:', payload.type);
      }
    } catch (error) {
      console.error('Error parsing WS message:', error);
      this.broadcaster.sendToId(this.clientId, {
        type: 'error',
        payload: {
          id: this.clientId,
          message: 'Invalid message format',
        },
      });
    }
  };

  private handlerClose = () => {
    this.broadcaster.broadcastExceptId(this.clientId, {
      type: 'device_disconnected',
      payload: this.clientId,
    });
    delete SessionHandler.connections[this.clientId];
    delete SessionHandler.cursors[this.clientId];
    delete SessionHandler.deviceInfo[this.clientId];
  };

  private handlerError = () => {
    this.broadcaster.close();
    delete SessionHandler.connections[this.clientId];
    delete SessionHandler.cursors[this.clientId];
    delete SessionHandler.deviceInfo[this.clientId];
  };
}
