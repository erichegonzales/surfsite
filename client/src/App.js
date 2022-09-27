import './App.css';
import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import PostFeed from "./components/PostFeed";
import Profile from "./components/Profile";
import Scroll from "./components/scroll_example/Scroll";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Navigation />
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/feed" element={<PostFeed />} />
        <Route exact path="/scroll" element={<Scroll />} />
        <Route exact path="/profile" element={<Profile />} />
      </Routes>
    </div>
  );
}

export default App;
