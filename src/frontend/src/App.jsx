import UsersList from '../../components/UsersList.jsx';
import PostsList from '../../components/PostsList.jsx';

export default function App() {
  return (
    <div className="app">
      <h1>Fullstack App — Users &amp; Posts</h1>
      <div className="grid">
        <UsersList />
        <PostsList />
      </div>
    </div>
  );
}
