import React from "react";

const FilmOption = ({ film, handleFilmClick, index }) => {
  return (
    <div key={index} className={`film-option_${index + 1}`}>
      <div
        className="film-poster"
        alt={film.Film_title}
        style={{ backgroundImage: `url(${film.Poster_url})` }}
      />
      <div className="film-info flex-left">
        <div className="two-line-container secondary">
          <h2 className="film-info__title t-preview-text secondary">
            {film.Film_title}
          </h2>
        </div>
        <p className="film-info__director body-text">{film.Director}</p>
        <div className="film-info__details body-text">
          <p className="film-info__runtime">{film.Runtime}</p>
          <p className="film-info__date">{film.Release_year}</p>
        </div>
        <div className="four-line-container body-text">
          <p
            className="film-info__synopsis p-preview-text body-text fw-skinny"
            onClick={() => handleFilmClick(film)}
          >
            {film.Synopsis}
          </p>
        </div>
      </div>
    </div>
  );
};

export default FilmOption;
