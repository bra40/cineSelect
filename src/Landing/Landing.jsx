import React from "react";
import "./landing.scss";
import { ReactComponent as MySvg } from "../Assets/PartnersIcon/partners.svg";

function Landing() {
  return (
    <div className="full-vh LandingComponentContainer">
      <div className="LandingSVGContainer padding-3">
        <MySvg />
      </div>
      <div className="LandingHeaderContainer flex-center">
        <header className="padding-3-block">
          <div className="Cine-Select-Title base-title">
            <h1 className="text-center">CINÉ</h1>
            <h1 className="text-center">SELECT</h1>
          </div>
        </header>
        <div className="padding-3-block">
          <main className="LandingTextContainer">
            <h2 className="base-sub">
              Find the right movie by rating film options
            </h2>
            <button className="base-button style-button">
              Today's Directors
            </button>
          </main>
        </div>
      </div>
      <footer className="flex-footer LandingFooter">
        <p className="base-body">Film Data Sourced (Not Endorsed) By TMDb</p>
      </footer>
    </div>
  );
}

export default Landing;
