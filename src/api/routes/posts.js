const express = require('express');
const router = express.Router();

let posts = [
  { id: 1, title: 'Getting Started with React', body: 'React is a powerful library for building user interfaces...', userId: 1, createdAt: '2024-01-20T11:00:00Z' },
  { id: 2, title: 'Node.js Best Practices', body: 'When building Node.js applications, there are several key principles...', userId: 2, createdAt: '2024-02-25T14:00:00Z' },
  { id: 3, title: 'REST API Design', body: 'Designing a clean REST API requires careful thought about resources...', userId: 1, createdAt: '2024-03-15T10:30:00Z' },
];

let nextId = 4;

// GET /api/posts
router.get('/', (req, res) => {
  res.json(posts);
});

// POST /api/posts
router.post('/', (req, res) => {
  const { title, body, userId } = req.body;
  if (!title || !body || !userId) {
    return res.status(400).json({ error: 'title, body, and userId are required' });
  }
  const post = { id: nextId++, title, body, userId: parseInt(userId), createdAt: new Date().toISOString() };
  posts.push(post);
  res.status(201).json(post);
});

// GET /api/posts/:id
router.get('/:id', (req, res) => {
  const post = posts.find(p => p.id === parseInt(req.params.id));
  if (!post) return res.status(404).json({ error: 'Post not found' });
  res.json(post);
});

// PUT /api/posts/:id
router.put('/:id', (req, res) => {
  const idx = posts.findIndex(p => p.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: 'Post not found' });
  const { title, body, userId } = req.body;
  posts[idx] = {
    ...posts[idx],
    ...(title && { title }),
    ...(body && { body }),
    ...(userId && { userId: parseInt(userId) }),
  };
  res.json(posts[idx]);
});

// DELETE /api/posts/:id
router.delete('/:id', (req, res) => {
  const idx = posts.findIndex(p => p.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: 'Post not found' });
  const deleted = posts.splice(idx, 1)[0];
  res.json(deleted);
});

module.exports = router;
