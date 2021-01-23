import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import FooterComponent from "./components/FooterComponent";
import Home from "./components/Home";
import LoginComponent from "./components/Login";
import NavbarComponent from "./components/NavbarComponent";
import "./stylesheet/App.scss";

function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <BrowserRouter>
        <Switch>
          <Route path="/home">
            <Home />
          </Route>
          <Route path="/login">
            <LoginComponent />
          </Route>
        </Switch>
      </BrowserRouter>
      <FooterComponent />
    </div>
  );
}

export default App;
