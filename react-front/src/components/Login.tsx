import React, { useState } from "react";
import { connect } from "react-redux";
import { LoginRequest } from "../models/UserModel";
import "../stylesheet/Login.scss";

interface IProps {
  login: ({ email, password }: LoginRequest) => void;
}

function LoginComponent(props: IProps) {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string>("");

  const submitForm = () => {
    if (email === "" || password === "") {
      setError("Fields are required");
      return;
    }
    props.login({ email, password });
  };

  return (
    <div className="h-100 w-100 row align-items-center d-flex justify-content-start">
      <form className="w-50 h-50 buttons-container p-3">
        <h3 className="mb-5">Log in</h3>
        <div className="w-50 h-50 center">
          <div className="form-group">
            <label>Email</label>
            <input
              onChange={(event) => {
                setEmail(event.target.value);
              }}
              value={email}
              type="email"
              className="form-control"
              placeholder="Enter email"
            />
          </div>

          <div className="form-group mb-5">
            <label>Password</label>
            <input
              onChange={(event) => {
                setPassword(event.target.value);
              }}
              value={password}
              type="password"
              className="form-control"
              placeholder="Enter password"
            />
          </div>
          <button
            type="button"
            className="btn btn-dark btn-lg btn-block"
            onSubmit={submitForm}
          >
            Sign in
          </button>
        </div>
      </form>
    </div>
  );
}
const mapDispatchToProps = {
  login: UserSlice.actions.start,
};

export default connect(null, mapDispatchToProps)(LoginComponent);
