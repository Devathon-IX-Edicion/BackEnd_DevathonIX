/src
├── api/                  ← Todas tus rutas HTTP organizadas por dominio
│   ├── chat/
│   │   └── routes.ts     ← GET /api/chat/history, POST /api/chat/send
│   ├── users/
│   │   └── routes.ts     ← CRUD de usuarios
│   └── index.ts          ← Enruta todo lo de /api
│
├── ws/                   ← WebSocket handlers
│   ├── chat/             ← Namespace o tipo de WebSocket (chat, live-updates, etc.)
│   │   ├── ChatRoom.ts   ← Durable Object por sala (o múltiples)
│   │   ├── ChatService.ts
│   │   └── WebSocketHandler.ts
│   └── index.ts          ← Enruta o despacha sockets según URL o DO
│
├── core/                 ← Utilidades reutilizables
│   ├── WebSocketManager.ts
│   ├── logger.ts
│   └── constants.ts
│
├── models/               ← Tipos y esquemas compartidos
│   ├── Message.ts
│   └── User.ts
│
├── utils/                ← Funciones auxiliares
│   └── formatMessage.ts
│
├── middleware/           ← Validadores, autenticación, etc.
│   └── withAuth.ts
│
├── config/               ← Config global (env vars, DO bindings, etc.)
│   └── env.ts
│
└── index.ts              ← Entrypoint del Worker (llama a api/index y ws/index)
