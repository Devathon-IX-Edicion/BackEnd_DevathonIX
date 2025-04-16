import { DurableObject } from 'cloudflare:workers';

export type Env = {
  Bindings: {
    MY_DURABLE_OBJECT: DurableObjectNamespace<MyDurableObject>;
  };
  Variables: {
    stub: DurableObjectStub<MyDurableObject>;
  };
};

export class MyDurableObject extends DurableObject {
  ctx: DurableObjectState;
  env: Env;
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    this.ctx = ctx;
    this.env = env;

    this.ctx.storage.sql.exec(`
            CREATE TABLE IF NOT EXISTS apple (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                greeting TEXT NOT NULL
            )
        `);

    const count = this.ctx.storage.sql.exec('SELECT COUNT(*) as count FROM apple').one().count;
    if (count === 0) {
      this.ctx.storage.sql.exec("INSERT INTO apple (greeting) VALUES ('Hello, World!')");
    }
  }

  async sayHello() {
    const result = this.ctx.storage.sql
      .exec('SELECT greeting FROM apple ORDER BY id DESC LIMIT 1')
      .one();
    return result?.greeting ?? 'Hello, World!';
  }

  async setText(text: string) {
    this.ctx.storage.sql.exec('INSERT INTO apple (greeting) VALUES (?)', [text]);
    return text;
  }
}
