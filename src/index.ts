export { MyDurableObject } from './counter';
import { Hono } from 'hono';
import { Env } from './counter';
import wsRoute from './routes/ws';

const app = new Hono<Env>();

app.route('/ws', wsRoute);

type Header = {
  'accept-encoding': string;
  'cf-connecting-ip': string;
  'cf-ipcountry': string;
  'cf-ray': string;
  'cf-visitor': string;
  connection: string;
  'content-length': string;
  'content-type': string;
  host: string;
  'user-agent': string;
  'x-forwarded-proto': string;
  'x-real-ip': string;
};

app.get('/', async (c) => {
  const id = c.env.MY_DURABLE_OBJECT.idFromName(new URL(c.req.url).pathname);
  const stub = c.env.MY_DURABLE_OBJECT.get(id);
  const greeting = await stub.sayHello();

  const headers: Partial<Header> = {
    'cf-connecting-ip': c.req.header('cf-connecting-ip') ?? undefined,
    'cf-ipcountry': c.req.header('cf-ipcountry') ?? undefined,
    'user-agent': c.req.header('user-agent') ?? undefined,
    'x-forwarded-proto': c.req.header('x-forwarded-proto') ?? undefined,
    'x-real-ip': c.req.header('x-real-ip') ?? undefined,
  };

  return c.json({
    greeting: greeting,
    url: c.req.url,
    name: new URL(c.req.url).pathname,
    stub: stub,
    id: id,
    headers,
  });
});

app.post('/', async (c) => {
  const id = c.env.MY_DURABLE_OBJECT.idFromName(new URL(c.req.url).pathname);
  const stub = c.env.MY_DURABLE_OBJECT.get(id);
  const body = await c.req.json();
  const greeting = await stub.setText(body.greeting);
  return c.json({
    greeting: greeting,
    url: c.req.url,
    name: new URL(c.req.url).pathname,
    stub: stub,
    id: id,
    env: c.env,
    body: body,
  });
});

export default app;
