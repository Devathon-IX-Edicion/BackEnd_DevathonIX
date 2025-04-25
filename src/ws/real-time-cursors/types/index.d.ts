export interface ENV_REALTIME_CURSORS {
  REALTIME_CURSORS: DurableObjectNamespace<RealTimeCursors>;
}
type DeviceInfo = {
  region: string;
  color: string;
};

export interface CursorPosition {
  x: number;
  y: number;
  rotation: number;
}

type DEVICE_ID = string;

export type CordsMause = Record<DEVICE_ID, CursorPosition>;
export type IDevices = Record<DEVICE_ID, DeviceInfo>;

export type DEVICE_CONNECTION = {
  devices: IDevices;
  cordsMause: CordsMause;
} & { id: DEVICE_ID };

export type DEVICE_DISCONNECTION = DEVICE_ID;
export type DEVICE_JOINED = Record<DEVICE_ID, DeviceInfo>;
export type DEVICE_CURSOR_MOVED = Record<DEVICE_ID, CursorPosition>;
export type DEVICE_ERROR = { id: DEVICE_ID; message: string };

export type RealTimeCursorEvent =
  | {
      type: 'device_connected';
      payload: DEVICE_CONNECTION;
    }
  | {
      type: 'device_disconnected';
      payload: DEVICE_DISCONNECTION;
    }
  | {
      type: 'device_joined';
      payload: DEVICE_JOINED;
    }
  | {
      type: 'cursor_moved';
      payload: DEVICE_CURSOR_MOVED;
    }
  | {
      type: 'error';
      payload: DEVICE_ERROR;
    };
