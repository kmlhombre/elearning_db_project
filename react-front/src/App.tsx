import React from "react";
import "./stylesheet/App.scss";
import FooterComponent from "./components/FooterComponent";
import Login from "./components/Login";
import Home from "./components/Home";
import NavbarComponent from "./components/NavbarComponent";

function App() {
  const isUser = false;

  return (
    <div className="App">
      <NavbarComponent />
      {isUser ? <Home /> : <Login />}
      <FooterComponent />
    </div>
  );
}

export default App;
