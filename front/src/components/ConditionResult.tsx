import React, { useState } from "react";
type Props = {
  symptoms: string[];
  // method : ()=> void;
};
function ConditionResult(_prop: Props) {
  const [hidden , setHidden] = useState(false);
  console.log("props", _prop.symptoms);
  const array = [..._prop.symptoms];
  return (
    <div className="conditionContianer">
      <div className="listOfConditions">
        <h3>Conditions that match your symptoms</h3>
        <div
          className="condition"
          style={{ cursor :"pointer"}}
          onClick={() => {
            if (hidden == false) setHidden(true);
            else if (hidden == true) setHidden(false);
          }}
        >
          Condition
        </div>
      </div>
      <div className="conditionINFO">
        {hidden ? (
          <>
            <h3>condition</h3>
            <hr style={{ borderColor: "black", width: "90%" }} />
            <b>
              Diverticula are small pouches that bulge out from weak spots in
              colon walls. Over time, pressure and strain from passing hard
              stools causes these weak areas. The condition is common in people
              over age 40. Early studies found that diverticular disease was
              especially prevalent in people who didn’t get enough fiber in
              their diet. When bacteria and fecal matter get inside these
              pouches, they become inflamed, causing diverticulitis.
              Diverticulitis causes pain, cramping, infection, bleeding, holes
              in the colon walls, intestinal blockage, and other serious
              complications. Usually, pain medication and antibiotics relieve
              symptoms of diverticulitis. Severe cases may require surgery.
            </b>
          </>
        ) : (
          <>
            <p>hi</p>
            {array.map((itam) => {
              console.log(itam);
              <div>
                <a href="">{itam}</a>
              </div>;
            })}
          </>
        )}
      </div>
    </div>
  );
}

export default ConditionResult;
