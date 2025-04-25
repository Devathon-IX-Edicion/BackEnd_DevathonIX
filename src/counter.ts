export class CounterDO {
  state: DurableObjectState;
  count: number = 0;

  constructor(state: DurableObjectState) {
    this.state = state;
    this.state.blockConcurrencyWhile(async () => {
      const stored = await this.state.storage.get<number>('count');
      this.count = stored || 0;
    });
  }

  async fetch(request: Request): Promise<Response> {
    const { pathname } = new URL(request.url);

    if (pathname === '/increment') {
      this.count++;
      await this.state.storage.put('count', this.count);
      return new Response(JSON.stringify({ count: this.count }), {
        headers: { 'Content-Type': 'application/json' },
      });
    }

    if (pathname === '/current') {
      return new Response(JSON.stringify({ count: this.count }), {
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return new Response('Not Found', { status: 404 });
  }
}
