import './App.css';
import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import PostsFeed from "./components/PostsFeed";
import ScrollExample from "./components/scroll_example/Scroll";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Navigation />
      <Routes>
        <Route exact path="/" element={<Landing />} />
        <Route exact path="/postsfeed" element={<PostsFeed />} />
        <Route exact path="/scroll" element={<ScrollExample />} />
      </Routes>
    </div>
  );
}

export default App;
