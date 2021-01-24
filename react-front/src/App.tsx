import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import ChangePassword from "./components/ChangePassword";
import FooterComponent from "./components/FooterComponent";
import Home from "./components/home/Home";
import LoginComponent from "./components/Login";
import NavbarComponent from "./components/NavbarComponent";
import Settings from "./components/Settings";
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
          <Route path="/settings">
            <Settings />
          </Route>
          <Route path="/change-password">
            <ChangePassword />
          </Route>
        </Switch>
      </BrowserRouter>
      <FooterComponent />
    </div>
  );
}

export default App;
