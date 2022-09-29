import './App.css';
import { Container } from "react-bootstrap"
import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import PostFeed from "./components/PostFeed";
import Profile from "./components/Profile";
import Logo from "./components/Logo";
import Loader from "./components/Loader";
import CreatePost from "./components/CreatePost";
import CreateLesson from "./components/CreateLesson";
import LessonListings from "./components/LessonListings";
import NewsFeed from "./components/NewsFeed";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Container className="App">
      <Navigation />
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/feed" element={<PostFeed />} />
        <Route exact path="/profile" element={<Profile />} />
      </Routes>
    </Container>
  );
}

export default App;
