import { dataDishes } from '~/src/data/dishes';
import { generatePastelColor } from '~/src/utils/generatePastelColor';
import { DeviceInfo, RealTimeCursorEvent } from '.';
import { WebSocketBroadcaster } from './WebSocketBroadcaster';
import { dataIngredients } from '~/src/data/ingredientes';

export class ConnecHandler {
  private static connections: Record<string, WebSocket> = {};
  private static deviceInfo: Record<string, DeviceInfo> = {};
  private broadcaster: WebSocketBroadcaster;
  private clientId: string;

  constructor() {
    this.clientId = crypto.randomUUID();
    this.broadcaster = new WebSocketBroadcaster(ConnecHandler.connections, this.clientId);
  }

  handle(ws: WebSocket, region: string) {
    ws.accept();

    ConnecHandler.connections[this.clientId] = ws;
    ConnecHandler.deviceInfo[this.clientId] = { region, color: generatePastelColor() };

    this.broadcaster.send({
      type: 'device_connected',
      payload: {
        devices: ConnecHandler.deviceInfo,
        id: this.clientId,
        ingredients: dataIngredients,
      },
    });

    this.broadcaster.broadcastExcept({
      type: 'device_joined',
      payload: { [this.clientId]: ConnecHandler.deviceInfo[this.clientId] },
    });

    ws.addEventListener('message', this.handlerMessage);
    ws.addEventListener('close', this.handlerClose);
    ws.addEventListener('error', this.handlerError);
  }

  private handlerMessage = (e: MessageEvent) => {
    try {
      const payload: RealTimeCursorEvent = JSON.parse(e.data.toString());
      switch (payload.type) {
        case 'fetch_dish': {
          const { ingredients } = payload.payload;
          const [dishes] = dataDishes.filter((dish) =>
            dish.ingredients.every((ingredient) => ingredients.includes(ingredient)),
          );

          if (!dishes) {
            this.broadcaster.send({
              type: '404',
              payload: 'No dishes found with the provided ingredients',
            });
          } else {
            this.broadcaster.send({
              type: 'request_dish',
              payload: {
                dishe: dishes,
              },
            });
          }
          break;
        }
        case 'fetch_ingredients': {
          console.log('Fetching ingredients...');
          this.broadcaster.send({
            type: 'request_ingredients',
            payload: dataIngredients,
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
    delete ConnecHandler.connections[this.clientId];
    delete ConnecHandler.deviceInfo[this.clientId];
  };

  private handlerError = () => {
    this.broadcaster.close();
    delete ConnecHandler.connections[this.clientId];
    delete ConnecHandler.deviceInfo[this.clientId];
  };
}
