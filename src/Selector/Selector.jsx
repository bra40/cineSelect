import React from "react";
import "./selector.scss";

function Selector() {
  return (
    <div>
      <div className="flex-center">
        <h3 className="base-sub">click to rank</h3>
        <h2 className="base-sub">User One’s Preferences</h2>
        <button className="SelectorButtonNext base-button style-button">
          Next
        </button>
      </div>
      <div className="SelectorContainer">
        <div className="poster-one">
          <img src="" alt="" className="poster-one" />
        </div>
        <div className="poster-two">
          <img src="" alt="" className="poster-two" />
        </div>
        <div className="poster-three">
          <img src="" alt="" className="poster-one" />
        </div>
        <div className="num-one">
          <h1 className="rank-a base-title">#</h1>
        </div>
        <div className="num-two">
          <h1 className="rank-b base-title">#</h1>
        </div>
        <div className="num-three">
          <h1 className="rank-c base-title">#</h1>
        </div>
      </div>
    </div>
  );
}

export default Selector;
