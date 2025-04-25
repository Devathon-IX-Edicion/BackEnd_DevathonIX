import { Hono } from 'hono';

const routeDevice = new Hono();

routeDevice.get('/', (c) => {
  const devices = [
    { id: 1, name: 'Device 1' },
    { id: 2, name: 'Device 2' },
    { id: 3, name: 'Device 3' },
  ];
  return c.json(devices);
});

export default routeDevice;
