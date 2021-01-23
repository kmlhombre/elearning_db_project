import React, { useCallback } from "react";
import Button from "react-bootstrap/esm/Button";
import { useHistory } from "react-router";
import "../stylesheet/Settings.scss";

function Settings() {
  const history = useHistory();

  const onChangePasswordClick = useCallback(
    () => history.push(`/change-password`),
    [history]
  );

  return (
    <div className="h-100 w-100 row align-items-center d-flex justify-content-center">
      <div className="w-50 h-25 row align-items-center buttons-container ">
        <Button size="lg" block variant="link" onClick={onChangePasswordClick}>
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
