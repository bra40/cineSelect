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
      <div className="SelectorContainer">
        {films.map((film, index) => (
          <div key={index} className={`poster_${index + 1}`}>
            <img
              src={film.Poster_url}
              alt={film.Film_title}
              className={`poster__image_${index + 1}`}
            />
            <div className="film-info flex-left">
              <h2 className="film-info__title primary title-wrap">
                {film.Film_title}
              </h2>
              <div className="film-info__details secondary">
                <p className="film-info__director">{film.Director}</p>
                <p className="film-info__date">{film.Release_year}</p>
              </div>
              <p className="film-info__synopsis p-preview-text p-wrap secondary">
                {film.Synopsis}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Selector;