import { useState } from "react";
import { doesExist } from "./myFunctions";
import Button from "./Button";
import { FaClipboardList, FaStethoscope, FaTrash } from "react-icons/fa";
import HiddenTextComponent from "./HiddenTextComponent";
import AddButton from "./AddButton";
import ConditionResult from "./ConditionResult";

function Tabe() {
  const [hidden, setHidden] = useState(false);
  const [activeTab, setActiveTab] = useState("tab1");
  const arrayListe = [
    "skinny arms",
    "pale skin",
    "shedding skin",
    "red skin",
    "yellow skin",
  ];
  const [value, setValue] = useState<string[]>([...arrayListe]);
  const [Symptom, setSymptom] = useState<string[]>([]);
  const [input, setInput] = useState<string>("");
  const deleteSymptom = (inde: number) => {
    setSymptom(
      Symptom.filter((syt, index) => {
        if (index != inde) return syt;
      })
    );
  };
  const storSymoptns = () => {
    if (input == "") {
      return;
    } else if (doesExist(input, Symptom)) {
      setInput("");
      return;
    }
    setSymptom([...Symptom, input]);
    setInput("");
  };
  const addSymptom = (e: string) => {
    const vare = e;
    if (doesExist(vare, Symptom)) {
      setInput("");
      return;
    }
    setSymptom([...Symptom, vare]);
    setInput("");
  };
  //  Functions to handle Tab Switching
  const handleTab1 = () => {
    // update the state to tab1
    setActiveTab("tab1");
  };
  const handleTab2 = () => {
    // update the state to tab2
    setActiveTab("tab2");
  };
  const handleTab3 = () => {
    // update the state to tab3
    setActiveTab("tab3");
  };

  const handleTabs = () => {
    if (activeTab === "tab1") {
      return (
        <>
          <div className="FirstTab">
            <div className="Form-group" style={{padding:"30px"}}>
              <h1>Symptom Checker</h1>
              <p>
                Identify possible conditions and treatment related to your
                symptoms.
              </p>
              <HiddenTextComponent />
            </div>
            <div className="toTab2">
              <Button
                onClick={() => {
                  handleTab2();
                }}
              />
            </div>
          </div>
        </>
      );
    } else if (activeTab === "tab2") {
      return (
        <div className="SecondTab">
          <div className="InputField">
            <h2>What are your symptoms?</h2>
            <input
              color="primary"
              type="text"
              placeholder="Enter Symptom..."
              name="text"
              className="input"
              value={input}
              onInput={(e) => {
                const inp = e.target as HTMLInputElement;
                setInput(inp.value);
                if (input.length >= 2) {
                  setHidden(true);
                } 
                if (input.length <= 1) {
                  setHidden(false);
                }
                if(input == ""){
                  setHidden(false);
                }
              }}
            />
          </div>
          <>
            {hidden && (
              <div className="SymptomList">
                  {value
                  .filter(itam => itam.includes(input))
                  .map((itame, index) => (
                    <div className="SymptomItem">
                      <>
                        <li>
                          <a
                            className="dropdown-item"
                            style={{ marginLeft: "20px" }}
                          >
                            {itame}
                          </a>
                        </li>
                      <AddButton
                        onClick={() => {
                          addSymptom(itame);
                          setHidden(false);
                        }}
                      />
                      </> 
                    </div>
                  ))}
              </div>
            )}
          </>
          <div
            className={`SymptomsContent ${Symptom.length === 0 ? "grid" : ""}`}
          >
            {Symptom.length == 0 ? (
              <>
                <FaStethoscope className="icon scope" />
                <FaClipboardList className="icon board" />
                <span>No symptoms added</span>
              </>
            ) : (
              <div className="symptomsBox">
                <h2>My Symptoms</h2>
                {Symptom.map((syt, index) => (
                  <>
                    <div className="singleSymptom">
                      {syt}
                      <button
                        className="ButtonFordelete"
                        onClick={() => {
                          deleteSymptom(index);
                        }}
                      >
                        <FaTrash />
                      </button>
                    </div>
                    <hr style={{ borderColor: "gray", width: "100%" }} />
                  </>
                ))}
              </div>
            )}
          </div>
          <div className="toTab3">
            <Button onClick={handleTab3} />
          </div>
        </div>
      );
    } else if (activeTab === "tab3") {
      return (
        <div className="ThirdTab">
          {/* <div className="ConditionContent">
            <p>See your Result!!</p>
          </div> */}
          <ConditionResult symptoms={Symptom} />
        </div>
      );
    }
  };
  return (
    <div className="Tabs">
      {/* Tab nav */}
      <ul className="nav">
        <li
          className={activeTab === "tab1" ? "active" : ""}
          onClick={handleTab1}
        >
          INFO
        </li>
        <li
          className={activeTab === "tab2" ? "active" : ""}
          onClick={handleTab2}
        >
          SYMPTOM
        </li>
        <li
          className={activeTab === "tab3" ? "active" : ""}
          onClick={handleTab3}
        >
          CONDITIONS
        </li>
      </ul>
      <div className="outlet">
        {/* content will be shown here */}
        {handleTabs()}
      </div>
    </div>
  );
}
export default Tabe;
