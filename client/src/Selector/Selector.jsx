import React, { useState, useEffect } from "react";
import "./selector.scss";

function Selector() {
  const [films, setFilms] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/film_dict")
      .then((response) => response.json())
      .then((films) => setFilms(films));
  }, []);

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
        {films.map((film, index) => (
          <div key={index} className={`poster-${index + 1}`}>
            <img
              src={film.Poster_url}
              alt={film.Film_title}
              className={`poster-${index + 1}`}
            />
            <div className="film-info">
              <h2>{film.Film_title}</h2>
              <p>
                {film.Director} ({film.Release_year})
              </p>
              <p>{film.Synopsis}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Selector;