import React from "react";
import "../stylesheet/Login.scss";

function LoginComponent() {
  return (
    <div className="h-100 w-100 row align-items-center d-flex justify-content-start">
      <form className="w-50 h-50 buttons-container p-3">
        <h3 className="mb-5">Log in</h3>
        <div className="w-50 h-50 center">
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              className="form-control"
              placeholder="Enter email"
            />
          </div>

          <div className="form-group mb-5">
            <label>Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter password"
            />
          </div>
          <button type="button" className="btn btn-dark btn-lg btn-block">
            Sign in
          </button>
        </div>
      </form>
    </div>
  );
}

export default LoginComponent;
