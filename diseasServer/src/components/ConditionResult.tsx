import React, { useState } from "react";
import Loader from "./Loader";
type Props = {
  condition:string;
  description:string;
  loading:boolean;
};
function ConditionResult(_prop: Props) {
  return (
    <div className="conditionContianer">
      {_prop.loading && <Loader />} {/* Conditionally render the Loader */}
      {_prop.answer && !_prop.loading && (
          <div className="listOfConditions">
            <h3>Conditions that match your symptoms</h3>
            <div
              className="condition"
              style={{ cursor: "pointer" }}
            >
              {_prop.answer}
            </div>
          </div>
      )}{" "}
    </div>
  );
}

export default ConditionResult;
