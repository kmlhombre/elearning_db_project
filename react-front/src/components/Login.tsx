import React from "react";
import { Button } from "react-bootstrap";
import ButtonGroup from "react-bootstrap/esm/ButtonGroup";
import Form from "react-bootstrap/esm/Form";
import "../stylesheet/Login.scss";

function LoginComponent() {
  return (
    <form className="mt-50 w-50 d-inline-block">
      <h3>Log in</h3>

      <div className="form-group">
        <label>Email</label>
        <input
          type="email"
          className="form-control"
          placeholder="Enter email"
        />
      </div>

      <div className="form-group">
        <label>Password</label>
        <input
          type="password"
          className="form-control"
          placeholder="Enter password"
        />
      </div>

      <div className="d-flex justify-content-around mb-3 mt-3">
        <Form.Check
          type="radio"
          label="Student"
          name="personGroup"
          id="radioStudent"
        />
        <Form.Check
          type="radio"
          label="Teacher"
          name="personGroup"
          id="radioTeacher"
        />
        <Form.Check
          type="radio"
          label="Parent"
          name="personGroup"
          id="radioParent"
        />
      </div>
      <button type="submit" className="btn btn-dark btn-lg btn-block">
        Sign in
      </button>
      <p className="forgot-password text-right">
        Forgot <a href="#">password?</a>
      </p>
    </form>
  );
}

export default LoginComponent;
