import React, { useState } from 'react';
import './styles.css';

function App() {
  const [query, setQuery] = useState('');
  const [style, setStyle] = useState('brief');
  const [books, setBooks] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');
    try {
      const response = await fetch('http://localhost:8000/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, style }),
      });
      if (!response.ok) {
        throw new Error('Failed to fetch recommendations');
      }
      const data = await response.json();
      setBooks(data);
    } catch (err) {
      setError('Error fetching recommendations');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">BookBuddy</h1>
      <div className="mb-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your book preferences (e.g., fantasy, detective)"
          className="border p-2 w-full mb-2"
        />
        <select
          value={style}
          onChange={(e) => setStyle(e.target.value)}
          className="border p-2 w-full mb-2"
        >
          <option value="brief">Brief</option>
          <option value="detailed">Detailed</option>
        </select>
        <button
          onClick={handleSubmit}
          className="bg-blue-500 text-white p-2 rounded"
        >
          Get Recommendations
        </button>
      </div>
      {error && <p className="text-red-500">{error}</p>}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {books.map((book, index) => (
          <div key={index} className="border p-4 rounded shadow">
            <h2 className="text-xl font-semibold">{book.title}</h2>
            <p className="text-gray-600">by {book.author}</p>
            <p className="text-gray-600">Genre: {book.genre}</p>
            <p>{book.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
