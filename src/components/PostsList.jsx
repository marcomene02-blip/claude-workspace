import { useEffect, useState } from 'react';

const API = 'http://localhost:4000/api';

export default function PostsList() {
  const [posts, setPosts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/posts`)
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((e) => {
        setError(e.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="card">
      <h2>Posts</h2>
      {loading && <p className="loading">Loading...</p>}
      {error && <p className="error">Error: {error}</p>}
      {!loading && !error && posts.map((p) => (
        <div key={p.id} className="item">
          <strong>{p.title}</strong>
          <small>by user #{p.userId}</small>
          <p>{p.body}</p>
        </div>
      ))}
    </div>
  );
}
