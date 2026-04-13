const express = require('express');
const router = express.Router();

let users = [
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', createdAt: '2024-01-15T10:00:00Z' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', createdAt: '2024-02-20T12:00:00Z' },
  { id: 3, name: 'Carol White', email: 'carol@example.com', createdAt: '2024-03-10T09:00:00Z' },
];

let nextId = 4;

// GET /api/users
router.get('/', (req, res) => {
  res.json(users);
});

// POST /api/users
router.post('/', (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ error: 'name and email are required' });
  }
  const user = { id: nextId++, name, email, createdAt: new Date().toISOString() };
  users.push(user);
  res.status(201).json(user);
});

// GET /api/users/:id
router.get('/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});

// PUT /api/users/:id
router.put('/:id', (req, res) => {
  const idx = users.findIndex(u => u.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: 'User not found' });
  const { name, email } = req.body;
  users[idx] = { ...users[idx], ...(name && { name }), ...(email && { email }) };
  res.json(users[idx]);
});

// DELETE /api/users/:id
router.delete('/:id', (req, res) => {
  const idx = users.findIndex(u => u.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: 'User not found' });
  const deleted = users.splice(idx, 1)[0];
  res.json(deleted);
});

module.exports = router;
