# Build Summary — Fullstack Users & Posts App

## What was built

A working full-stack app with a REST API backend and a React frontend, both running locally.

- **Frontend:** http://localhost:3000 — React + Vite, two components (`UsersList`, `PostsList`) that fetch from the API and render cards.
- **Backend:** http://localhost:4000 — Node.js + Express REST API with in-memory storage.

### Backend endpoints
Base URL: `http://localhost:4000/api`

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/users` | List users |
| POST | `/users` | Create user (`{name, email}`) |
| GET | `/users/:id` | Get user |
| PUT | `/users/:id` | Update user |
| DELETE | `/users/:id` | Delete user |
| GET | `/posts` | List posts |
| POST | `/posts` | Create post (`{title, body, userId}`) |
| GET | `/posts/:id` | Get post |
| PUT | `/posts/:id` | Update post |
| DELETE | `/posts/:id` | Delete post |

Seeded with 3 users and 3 posts at startup. CORS enabled for `*`.

### File layout
```
src/
  api/
    server.js            Express entry, port 4000
    routes/users.js      Users CRUD
    routes/posts.js      Posts CRUD
    package.json
  components/
    UsersList.jsx        Fetches /api/users
    PostsList.jsx        Fetches /api/posts
  frontend/
    index.html           Vite entry
    vite.config.js       Port 3000, strictPort
    src/main.jsx         React bootstrap
    src/App.jsx          Imports ../../components/*
    src/styles.css
    package.json
tests/
  run-tests.js           18 integration tests (Node built-in fetch, no deps)
  report.md              Pass/fail results
docs/
  build-summary.md       (this file)
```

## Key decisions

1. **In-memory storage, not a DB.** Task scope didn't need persistence; arrays keep the setup friction-free.
2. **Separate ports (3000 frontend, 4000 backend).** Avoids the React vs. API collision on 3000 that the task implies.
3. **Components live in `src/components/`, Vite root is `src/frontend/`.** Task specifies both locations. Vite's `/@fs` handler serves files outside the root, so the App imports `../../components/*.jsx` and Vite resolves them correctly at dev time — no duplication, no symlinks.
4. **Test runner is plain `node tests/run-tests.js`** — no Jest/Vitest install. Uses Node's built-in `fetch` to hit real servers, so tests double as end-to-end integration coverage.
5. **No build step for the frontend.** Vite dev server is enough for the "running app" deliverable; `npm run build` still works if a production bundle is ever needed.
6. **Tests written directly (not by QA teammate).** The three spawned Sonnet teammates stalled on permission approvals and never produced output after ~1600s; I took over and built everything directly to hit the deliverable.

## How to run

### Backend
```bash
cd src/api
npm install       # only first time
node server.js    # serves http://localhost:4000
```

### Frontend
```bash
cd src/frontend
npm install       # only first time
npm run dev       # serves http://localhost:3000
```

Open http://localhost:3000 in a browser. The page shows a two-column grid: Users on the left, Posts on the right. Both populate from live backend calls.

### Tests
With both servers running:
```bash
node tests/run-tests.js
```
Rewrites `tests/report.md` with pass/fail counts. Current state: **18/18 passing**.

## Current running state

At build time:
- Backend process (`node server.js`) running in background on port 4000.
- Frontend process (`vite`) running in background on port 3000.
- All 18 tests passing.
