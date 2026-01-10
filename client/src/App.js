import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import Home from './pages/Home';
import MyPets from './pages/MyPets';
import BookSession from './pages/BookSession';

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/my-pets" element={<MyPets />} />
        <Route path="/book" element={<BookSession />} />
      </Routes>
    </Router>
  );
}