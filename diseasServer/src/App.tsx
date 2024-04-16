import Tabe from "./components/Tabe";
import "./App.css";
import SymptomSideBar from "./components/SymptomSideBar";
import { useState, useEffect } from "react";
import axios from "axios";
function App() {
  const [responseData, setResponseData] = useState<string[]>([]);
  useEffect(() => {
    const fetchDataFromBackend = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/getSymptoms/");
        setResponseData(response.data);
      } catch (error) {
        console.error("Error:", error);
      }
    };
    fetchDataFromBackend();
  }, []);
  return (
    <div className="App">
      <SymptomSideBar
        symptoms={[...JSON.parse(JSON.stringify(responseData))]}
      />
      <Tabe symptoms={[...JSON.parse(JSON.stringify(responseData))]} />
    </div>
  );
}
export default App;
