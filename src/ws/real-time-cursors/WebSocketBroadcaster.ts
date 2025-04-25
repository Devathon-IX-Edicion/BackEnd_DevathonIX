import { RealTimeCursorEvent } from './types';

export class WebSocketBroadcaster {
  private connections: Record<string, WebSocket>;
  private clientId: string;

  constructor(connections: Record<string, WebSocket>, clientId: string) {
    this.connections = connections;
    this.clientId = clientId;
  }

  send(message: RealTimeCursorEvent) {
    const conn = this.connections[this.clientId];
    if (conn) {
      conn.send(JSON.stringify(message));
    }
  }

  sendToId(id: string, message: RealTimeCursorEvent) {
    const conn = this.connections[id];
    if (conn) {
      conn.send(JSON.stringify(message));
    }
  }

  broadcastExcept(message: RealTimeCursorEvent) {
    Object.entries(this.connections).forEach(([connId, conn]) => {
      if (connId !== this.clientId) {
        conn.send(JSON.stringify(message));
      }
    });
  }

  broadcastExceptId(id: string, message: RealTimeCursorEvent) {
    Object.entries(this.connections).forEach(([connId, conn]) => {
      if (connId !== id) {
        conn.send(JSON.stringify(message));
      }
    });
  }

  broadcast(message: RealTimeCursorEvent) {
    Object.values(this.connections).forEach((conn) => {
      conn.send(JSON.stringify(message));
    });
  }

  // cierra la conexión del cliente actual.
  close() {
    const conn = this.connections[this.clientId];
    if (conn) {
      conn.close();
    }
  }
  // cierra la conexión de un cliente específico.
  closeClient(id: string) {
    const conn = this.connections[id];
    if (conn) {
      conn.close();
    }
  }
  // cierra todas las conexiones.
  closeAll() {
    Object.values(this.connections).forEach((conn) => {
      conn.close();
    });
  }
}
