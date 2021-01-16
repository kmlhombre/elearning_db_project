import React from "react";
import "./App.scss";
import FooterComponent from "./components/FooterComponent";
import NavbarComponent from "./components/NavbarComponent";

function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <FooterComponent />
    </div>
  );
}

export default App;
