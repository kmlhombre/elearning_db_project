import React from "react";
import { gradeMockArray } from "../../__mocks__/gradeMock";
import GradeRow from "./atoms/GradeRow";
import "../../stylesheet/Grade.scss";

function Home() {
  return (
    <div className="h-75 w-100 row align-items-center d-flex justify-content-center">
      <div>
        <p className="header">Your grades</p>
        <div className="d-flex flex-row justify-content-around title-container header-text">
          <span>Subject</span>
          <span>Note</span>
        </div>
        {gradeMockArray.map((item) => (
          <div key={item.id}>
            <GradeRow grade={item} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
