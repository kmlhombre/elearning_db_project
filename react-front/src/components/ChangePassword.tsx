import React from "react";

function ChangePassword() {
  return (
    <div className="h-100 w-100 row align-items-center d-flex justify-content-start">
      <form className="w-50 h-50 buttons-container p-3">
        <h3 className="mb-5">Change password</h3>
        <div className="w-50 h-50 center">
          <div className="form-group">
            <label>Current Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter current password"
            />
          </div>

          <div className="form-group mb-5">
            <label>New Password</label>
            <input
              type="password"
              className="form-control"
              placeholder="Enter new password"
            />
          </div>
          <button type="button" className="btn btn-dark btn-lg btn-block">
            Change password
          </button>
        </div>
      </form>
    </div>
  );
}

export default ChangePassword;
