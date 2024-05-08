import { useState,useEffect} from "react";
import "../components/sideBar.css";
import { FaBars,FaTimes } from "react-icons/fa";
import { sendData } from "./myFunctions";
import diseaseDesign from "../assets/diseaseDesign.png";
import Loader from "./Loader";
// import Tabe from "./Tabe";
const ToggleSidebarButton: React.FC<{ onClick: () => void }>=({
  onClick
}) => {
  return (
    <button className=" btn-primary" style={{cursor:"pointer"}} onClick={onClick}>
      <FaBars></FaBars>
    </button>
  );
};
type prop={
  symptoms:string[];
};
const SymptomSideBar  = ({symptoms}:prop) => {
  const [checkedItems, setCheckedItems] = useState<string[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [hidden, setHidden] = useState(false);
  const [showCondition, setShowCondition] = useState(false);
  const [filterName, setFilterName] = useState("");
  const [list, setList] = useState<string[]>([]);
  const [answer, setAnswer] = useState(String);
  useEffect(() => {
    setList([...symptoms]);
  }, [symptoms]);
  const toggleList = () => {
    setHidden(!hidden);
  };
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };
  const toggleConditionBar = () => {
    setShowCondition(!showCondition);
  };
  const handleCheckboxChange = (itemName: string) => {
    const isChecked = checkedItems.includes(itemName);
    if (isChecked) {
      // If item is already checked, remove it from the checked items
      setCheckedItems(checkedItems.filter((item) => item !== itemName));
    } else {
      // If item is not checked, add it to the checked items
      setCheckedItems([...checkedItems, itemName]);
    }
  };

  //handle loader animation
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const handleClick = () => {
    setIsLoading(true);

    // Simulate a delay to mimic fetching data
    setTimeout(() => {
      // Once data is fetched, set isLoading to false and display the result
      setIsLoading(false);
    }, 2000); // Adjust the time as per your requirement

    // You would typically perform an API call here
    console.log(isLoading);
  };
  return (
    <>
      <div style={{ position: "absolute", top: "0%", display: "flex" }}>
        <nav className="navbar navbar-expand-lg navbar-light bg-white shadow-md">
          <div className=" navContianer">
            <img
              src={diseaseDesign}
              alt=""
              style={{ width: "250px", height: "60px" }}
            />
            <div className="navButton">
              <ToggleSidebarButton onClick={toggleSidebar} />
            </div>
          </div>
        </nav>
        <div
          className={`sidebar ${isOpen ? "active" : ""}`}
          style={{
            display: "flex",
            flexDirection: "column",
            position: "fixed",
            zIndex: "2",
          }}
        >
          <div className="sd-header">
            <h4 className="mb-0">Symptoms by Body parts</h4>
            <div className="btn btn-primary" onClick={toggleSidebar}>
              <FaTimes className="faTimes" />
            </div>
          </div>
          <div className="sd-body">
            <ul>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("All");
                    setShowCondition(false);
                  }}
                >
                  All Symptoms
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("head");
                    setShowCondition(false);
                  }}
                >
                  Head
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("neck");
                    setShowCondition(false);
                  }}
                >
                  Neck
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("chest");
                    setShowCondition(false);
                  }}
                >
                  Chest
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("eyes");
                    setShowCondition(false);
                  }}
                >
                  Eyes
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setShowCondition(false);
                    setFilterName("skin");
                  }}
                >
                  Skin
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("back");
                    setShowCondition(false);
                  }}
                >
                  Back
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("leg");
                    setShowCondition(false);
                  }}
                >
                  Legs
                </a>
              </li>
              <li>
                <a
                  className="sd-link"
                  onClick={() => {
                    setHidden(true);
                    setFilterName("stomach");
                    setShowCondition(false);
                  }}
                >
                  Stomach
                </a>
              </li>
            </ul>
          </div>
          <div className="btnCoondition">
            <button
              className="btnx conditionC"
              onClick={() => {
                toggleConditionBar();
                handleClick();
                setHidden(false);
                sendData(checkedItems).then((result) => {
                  setAnswer(result);
                });
              }}
            >
              Condition
            </button>
          </div>
        </div>
        <div
          className={`sidebar-overlay ${isOpen ? "active" : ""}`}
          style={{ position: "fixed", zIndex: "1" }}
          onClick={() => {
            toggleSidebar();
            setShowCondition(false);
            setHidden(false);
          }}
        ></div>
        <>
          {hidden && (
            <>
              {filterName == "All" ? (
                <div className="listOfSymptoms">
                  <h3>List Of {filterName} Symptoms</h3>
                  <div className="symptoms">
                    {list.map((item, index) => (
                      <li key={index} className="listOfItames">
                        <input
                          type="checkbox"
                          id={item}
                          name={item}
                          className="checkBox"
                          checked={checkedItems.includes(item)} // Set checked attribute based on checkedItems state
                          onChange={() => handleCheckboxChange(item)}
                        />
                        <label htmlFor={item} className="label">
                          {item}
                        </label>
                      </li>
                    ))}
                  </div>
                  <div className="btnContianer">
                    <button className="btnx Done" onClick={toggleList}>
                      Done
                    </button>
                    <button className="btnx skip" onClick={toggleList}>
                      skip
                    </button>
                  </div>
                </div>
              ) : (
                <div className="listOfSymptoms">
                  <h3>List Of {filterName} Symptoms</h3>
                  <div className="symptoms">
                    {list
                      .filter((item) =>
                        item.toLowerCase().includes(filterName.toLowerCase())
                      )
                      .map((item, index) => (
                        <li key={index} className="listOfItames">
                          <input
                            type="checkbox"
                            id={item}
                            name={item}
                            className="checkBox"
                            checked={checkedItems.includes(item)} // Set checked attribute based on checkedItems state
                            onChange={() => handleCheckboxChange(item)}
                          />
                          <label htmlFor={item} className="label">
                            {item}
                          </label>
                        </li>
                      ))}
                  </div>
                  <div className="btnContianer">
                    <button className="btnx Done" onClick={toggleList}>
                      Done
                    </button>
                    <button className="btnx skip" onClick={toggleList}>
                      skip
                    </button>
                  </div>
                </div>
              )}
            </>
          )}
        </>
        <>
          {showCondition && (
            <div className="conditionContant">
              {isLoading && <Loader />} {/* Conditionally render the Loader */}
              {answer && !isLoading && (
                <>
                  <b>{answer}</b>
                </>
              )}{" "}
            </div>
          )}
        </>
      </div>
    </>
  );
};

export default SymptomSideBar;
