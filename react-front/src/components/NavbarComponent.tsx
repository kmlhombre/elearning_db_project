import React from "react";
import { Nav } from "react-bootstrap";
import Navbar from "react-bootstrap/Navbar";
import { Router, Switch, Route } from "react-router-dom";
import Home from "./home/Home";
import Settings from "./Settings";
import { createBrowserHistory } from "history";

const history = createBrowserHistory();

function NavbarComponent() {
  return (
    <Router history={history}>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="/">Class Register</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="/">Home</Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link href="/settings">Settings</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>

      <Switch>
        <Route exact path="/" component={Home} />
      </Switch>
      <Switch>
        <Route exact path="/settings" component={Settings} />
      </Switch>
    </Router>
  );
}

export default NavbarComponent;
