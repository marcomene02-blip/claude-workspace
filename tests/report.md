# Test Report

**Date:** 2026-04-13T16:32:51.765Z
**Summary:** 18 passed, 0 failed

## Environment
- Backend: http://localhost:4000
- Frontend: http://localhost:3000

## Results

| # | Test | Result |
|---|------|--------|
| 1 | GET /api/health returns ok | PASS |
| 2 | GET /api/users returns array with seed users | PASS |
| 3 | GET /api/users/:id returns single user | PASS |
| 4 | GET /api/users/:id returns 404 for missing | PASS |
| 5 | POST /api/users creates a user | PASS |
| 6 | POST /api/users validates required fields | PASS |
| 7 | PUT /api/users/:id updates a user | PASS |
| 8 | DELETE /api/users/:id removes a user | PASS |
| 9 | GET /api/posts returns array with seed posts | PASS |
| 10 | GET /api/posts/:id returns single post | PASS |
| 11 | POST /api/posts creates a post | PASS |
| 12 | POST /api/posts validates required fields | PASS |
| 13 | PUT /api/posts/:id updates a post | PASS |
| 14 | DELETE /api/posts/:id removes a post | PASS |
| 15 | CORS header present | PASS |
| 16 | Frontend serves HTML at localhost:3000 | PASS |
| 17 | Frontend serves App.jsx module | PASS |
| 18 | Frontend can reach UsersList component via /@fs | PASS |

## Status: All tests passed — app confirmed running at http://localhost:3000
