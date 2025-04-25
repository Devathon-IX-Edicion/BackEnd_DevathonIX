export interface ENV_DEVATHON {
  DEVATHON: DurableObjectNamespace<RealTimeCursors>;
}

type DeviceInfo = {
  region: string;
  color: string;
};

type DEVICE_ID = string;

export type IDevices = Record<DEVICE_ID, DeviceInfo>;

export type Dishe = {
  name: string;
  description: string;
  category: string;
  ingredients: number[];
  magic_level: string;
};

export interface Ingredient {
  name: string;
  slug: string;
  description: string;
  magic_level: string;
  preparation_time: number;
  category: string;
  date_created: string;
  id: number;
}

export type DEVICE_CONNECTION = {
  devices: IDevices;
  ingredients: Ingredient[];
} & { id: DEVICE_ID };

export type DEVICE_DISCONNECTION = DEVICE_ID;
export type DEVICE_JOINED = Record<DEVICE_ID, DeviceInfo>;
export type DEVICE_ERROR = { id: DEVICE_ID; message: string };
export type DEVICE_404 = string;

export type DEVICE_FETCH_DISH = { ingredients: number[] };
export type DEVICE_REQUEST_DISH = { dishe: Dishe };

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
      type: 'error';
      payload: DEVICE_ERROR;
    }
  | {
      type: 'fetch_ingredients';
    }
  | {
      type: 'request_ingredients';
      payload: Ingredient[];
    }
  | {
      type: 'fetch_dish';
      payload: DEVICE_FETCH_DISH;
    }
  | {
      type: 'request_dish';
      payload: DEVICE_REQUEST_DISH;
    }
  | {
      type: '404';
      payload: DEVICE_404;
    };
