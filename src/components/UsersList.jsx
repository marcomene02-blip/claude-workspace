import { useEffect, useState } from 'react';

const API = 'http://localhost:4000/api';

export default function UsersList() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/users`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((e) => {
        setError(e.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="card">
      <h2>Users</h2>
      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">Error: {error}</p>}
      {!loading && !error && users.map((u) => (
        <div key={u.id} className="item">
          <strong>{u.name}</strong>
          <small>{u.email}</small>
        </div>
      ))}
    </div>
  );
}
