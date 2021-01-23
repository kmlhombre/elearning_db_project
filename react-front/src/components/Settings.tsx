import React from "react";
import Button from "react-bootstrap/esm/Button";
import "../stylesheet/Settings.scss";

function Settings() {
  return (
    <div className="h-100 w-100 row align-items-center d-flex justify-content-center">
      <div className="w-50 h-25 row align-items-center buttons-container ">
        <Button size="lg" block variant="link">
          Change Password
        </Button>
        <Button size="lg" block variant="link">
          Logout
        </Button>
      </div>
    </div>
  );
}

export default Settings;
