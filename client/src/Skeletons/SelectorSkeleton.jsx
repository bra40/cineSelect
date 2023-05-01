import Skeleton, { SkeletonTheme } from "react-loading-skeleton";

import "../Selector/selector.scss";

import React from "react";

function SelectorSkeleton() {
  return (
    <div className="selector-container">
      <SkeletonTheme baseColor="#616161" highlightColor="#e9dfd0">
        <div className="film-section__">
          <div className="film-option_this">
            <div
              className="film-poster"
              style={{ backgroundColor: "#616161" }}
            />
            <div className="film-info">
              <div className="skeleton-container">
                <div className="skeleton-center">
                  <div className="skeleton-title">
                    <Skeleton
                      count={2}
                      style={{ height: "1.5em", marginBlockEnd: ".5em" }}
                    />
                  </div>
                </div>
              </div>
              <div className="skeleton-details">
                <div className="skeleton-name">
                  <Skeleton style={{ height: ".8em" }} />
                </div>
              </div>
              <div className="skeleton-details">
                <div className="skeleton-runtime">
                  <Skeleton style={{ height: ".8em" }} />
                </div>
                <div className="skeleton-right">
                  <div className="skeleton-date">
                    <Skeleton
                      style={{ height: ".8em", marginBlockEnd: ".2em" }}
                    />
                  </div>
                </div>
              </div>
              <div className="skeleton-container">
                <div className="skeleton-body">
                  <Skeleton count={4} style={{ height: ".6em" }} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </SkeletonTheme>
    </div>
  );
}

export default SelectorSkeleton;
