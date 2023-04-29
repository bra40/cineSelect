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
          // <div key={index} className={`poster_${index + 1}`}>
          <div className={`film_option_${index + 1}`}>
            <div className={`line_div_${index + 1}`} />
            <div key={index} className={`poster_${index + 1}`}>
              <div
                className="this_img_container"
                alt={film.Film_title}
                style={{ backgroundImage: `url(${film.Poster_url})` }}
              />
              <div className="film-info flex-left">
                <div className="two_line_container secondary">
                  <h2 className="film-info__title secondary">
                    {film.Film_title}
                  </h2>
                </div>
                <p className="film-info__director body-text">{film.Director}</p>
                <div className="film-info__details body-text">
                  <p className="film-info__runtime">{film.Runtime}</p>
                  <p className="film-info__date">{film.Release_year}</p>
                </div>
                <div className="four_line_container body-text">
                  <p className="film-info__synopsis p-preview-text body-text fw-skinny">
                    {film.Synopsis}
                  </p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Selector;