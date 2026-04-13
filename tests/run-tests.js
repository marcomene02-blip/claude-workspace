// Integration test suite — hits the running API at localhost:4000 and frontend at localhost:3000.
// Run with: node tests/run-tests.js
// Requires: API server running (src/api), Vite dev server running (src/frontend).

const API = 'http://localhost:4000/api';
const FRONTEND = 'http://127.0.0.1:3000';

const results = [];
let passed = 0;
let failed = 0;

async function test(name, fn) {
  try {
    await fn();
    results.push({ name, status: 'PASS', error: null });
    passed++;
    console.log(`  PASS  ${name}`);
  } catch (e) {
    results.push({ name, status: 'FAIL', error: e.message });
    failed++;
    console.log(`  FAIL  ${name}  — ${e.message}`);
  }
}

function assert(cond, msg) {
  if (!cond) throw new Error(msg || 'assertion failed');
}

async function json(url, opts) {
  const r = await fetch(url, opts);
  const body = await r.json().catch(() => null);
  return { status: r.status, body };
}

async function main() {
  console.log('--- Backend unit-shape tests ---');

  await test('GET /api/health returns ok', async () => {
    const { status, body } = await json(`${API}/health`);
    assert(status === 200, `expected 200, got ${status}`);
    assert(body.status === 'ok', 'health status not ok');
  });

  await test('GET /api/users returns array with seed users', async () => {
    const { status, body } = await json(`${API}/users`);
    assert(status === 200, `expected 200, got ${status}`);
    assert(Array.isArray(body), 'response is not an array');
    assert(body.length >= 3, `expected >=3 users, got ${body.length}`);
    assert(body[0].id && body[0].name && body[0].email, 'user shape invalid');
  });

  await test('GET /api/users/:id returns single user', async () => {
    const { status, body } = await json(`${API}/users/1`);
    assert(status === 200, `expected 200, got ${status}`);
    assert(body.id === 1, 'wrong user returned');
  });

  await test('GET /api/users/:id returns 404 for missing', async () => {
    const { status } = await json(`${API}/users/9999`);
    assert(status === 404, `expected 404, got ${status}`);
  });

  await test('POST /api/users creates a user', async () => {
    const { status, body } = await json(`${API}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'Test User', email: 'test@example.com' }),
    });
    assert(status === 201, `expected 201, got ${status}`);
    assert(body.id && body.name === 'Test User', 'created user invalid');
    global._testUserId = body.id;
  });

  await test('POST /api/users validates required fields', async () => {
    const { status } = await json(`${API}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'Missing email' }),
    });
    assert(status === 400, `expected 400, got ${status}`);
  });

  await test('PUT /api/users/:id updates a user', async () => {
    const { status, body } = await json(`${API}/users/${global._testUserId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'Updated Name' }),
    });
    assert(status === 200, `expected 200, got ${status}`);
    assert(body.name === 'Updated Name', 'update did not apply');
  });

  await test('DELETE /api/users/:id removes a user', async () => {
    const { status } = await json(`${API}/users/${global._testUserId}`, { method: 'DELETE' });
    assert(status === 200, `expected 200, got ${status}`);
    const check = await json(`${API}/users/${global._testUserId}`);
    assert(check.status === 404, 'user still exists after delete');
  });

  await test('GET /api/posts returns array with seed posts', async () => {
    const { status, body } = await json(`${API}/posts`);
    assert(status === 200, `expected 200, got ${status}`);
    assert(Array.isArray(body) && body.length >= 3, 'posts array invalid');
    assert(body[0].title && body[0].body && body[0].userId, 'post shape invalid');
  });

  await test('GET /api/posts/:id returns single post', async () => {
    const { status, body } = await json(`${API}/posts/1`);
    assert(status === 200, `expected 200, got ${status}`);
    assert(body.id === 1, 'wrong post');
  });

  await test('POST /api/posts creates a post', async () => {
    const { status, body } = await json(`${API}/posts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: 'T', body: 'B', userId: 1 }),
    });
    assert(status === 201, `expected 201, got ${status}`);
    global._testPostId = body.id;
  });

  await test('POST /api/posts validates required fields', async () => {
    const { status } = await json(`${API}/posts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: 'only title' }),
    });
    assert(status === 400, `expected 400, got ${status}`);
  });

  await test('PUT /api/posts/:id updates a post', async () => {
    const { status, body } = await json(`${API}/posts/${global._testPostId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: 'Updated Title' }),
    });
    assert(status === 200, `expected 200, got ${status}`);
    assert(body.title === 'Updated Title', 'post update did not apply');
  });

  await test('DELETE /api/posts/:id removes a post', async () => {
    const { status } = await json(`${API}/posts/${global._testPostId}`, { method: 'DELETE' });
    assert(status === 200, `expected 200, got ${status}`);
  });

  await test('CORS header present', async () => {
    const r = await fetch(`${API}/users`);
    const cors = r.headers.get('access-control-allow-origin');
    assert(cors === '*' || cors, `CORS header missing: ${cors}`);
  });

  console.log('--- Frontend tests ---');

  await test('Frontend serves HTML at localhost:3000', async () => {
    const r = await fetch(FRONTEND + '/');
    assert(r.status === 200, `expected 200, got ${r.status}`);
    const html = await r.text();
    assert(html.includes('<div id="root">'), 'root div missing');
    assert(html.includes('main.jsx'), 'main.jsx script missing');
  });

  await test('Frontend serves App.jsx module', async () => {
    const r = await fetch(FRONTEND + '/src/App.jsx');
    assert(r.status === 200);
    const src = await r.text();
    assert(src.includes('UsersList'), 'App does not import UsersList');
    assert(src.includes('PostsList'), 'App does not import PostsList');
  });

  await test('Frontend can reach UsersList component via /@fs', async () => {
    const r = await fetch(FRONTEND + '/@fs/C:/Users/marco/Desktop/Claude/src/components/UsersList.jsx');
    assert(r.status === 200, `expected 200, got ${r.status}`);
    const src = await r.text();
    assert(src.includes('fetch'), 'UsersList should use fetch');
  });

  console.log(`\nSummary: ${passed} passed, ${failed} failed`);

  // Write report
  const fs = await import('node:fs');
  const lines = [
    '# Test Report',
    '',
    `**Date:** ${new Date().toISOString()}`,
    `**Summary:** ${passed} passed, ${failed} failed`,
    '',
    '## Environment',
    '- Backend: http://localhost:4000',
    '- Frontend: http://localhost:3000',
    '',
    '## Results',
    '',
    '| # | Test | Result |',
    '|---|------|--------|',
    ...results.map((r, i) => `| ${i + 1} | ${r.name} | ${r.status === 'PASS' ? 'PASS' : 'FAIL: ' + r.error} |`),
    '',
    failed === 0
      ? '## Status: All tests passed — app confirmed running at http://localhost:3000'
      : `## Status: ${failed} test(s) failed`,
    '',
  ];
  fs.writeFileSync('tests/report.md', lines.join('\n'));
  console.log('Wrote tests/report.md');

  process.exit(failed === 0 ? 0 : 1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
