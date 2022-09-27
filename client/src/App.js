import './App.css';
import Navigation from "./components/Navigation";
import Landing from "./components/Landing";
import { Switch, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Navigation />
      <Landing />
    </div>
  );
}

export default App;
