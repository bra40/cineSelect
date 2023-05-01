import "./app.scss";
// import Landing from "./Landing/Landing";
import "react-loading-skeleton/dist/skeleton.css";
import Selector from "./Selector/Selector"
// import Recommendation from "./Recommendation/Recommendation"
// import Elements from "./Elements/Elements"

function App() {
  return (
    <div className="App">
      {/* <Landing/> */}
      {/* <Elements /> */}
      <Selector />
      {/* <Recommendation/> */}
    </div>
  );
}

export default App;
