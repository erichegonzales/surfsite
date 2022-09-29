import './App.css';
import { Container } from "react-bootstrap"
import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import PostFeed from "./components/PostFeed";
import Profile from "./components/Profile";
import LessonListings from "./components/LessonListings";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Container className="App">
      <Navigation />
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/profile" element={<Profile />} />
        <Route exact path="/posts" element={<PostFeed />} />
        <Route exact path="/lessons" element={<LessonListings />} />
      </Routes>
    </Container>
  );
}

export default App;
