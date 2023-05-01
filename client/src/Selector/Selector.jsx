import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import SelectorSkeleton from "../Skeletons/SelectorSkeleton"
import "./selector.scss";

function Selector() {
  const [films, setFilms] = useState([]);
  const [selectedFilm, setSelectedFilm] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/film_dict")
      .then((response) => response.json())
      .then((films) => setFilms(films));
  }, []);

  const handleFilmClick = (film) => {
    setSelectedFilm(film);
  };

  const handleAsideClose = () => {
    setSelectedFilm(null);
  };

  const handleDragEnd = (event, info) => {
    const { height } = event.target.getBoundingClientRect();
    const { y } = info.offset;

    if (y > height / 4) {
      handleAsideClose();
    }
  };

  return (
    <div>
      {/* <SelectorSkeleton /> */}
      <div className="flex-center selector-wrapper-padding">
        <h3 className="secondary lowercase">click to rank</h3>
        <h2 className="primary capitalize">user one’s preferences</h2>
      </div>
      <div className="SelectorContainer">
        {films.map((film, index) => (
          // <div key={index} className={`poster_${index + 1}`}>
          <div key={index} className={`film_option_${index + 1}`}>
            <div className={`line_div_${index + 1}`} />
            <div key={index} className={`poster_${index + 1}`}>
              <div
                className="this_img_container"
                alt={film.Film_title}
                style={{ backgroundImage: `url(${film.Poster_url})` }}
              />
              <div className="film-info flex-left">
                <div className="two_line_container secondary">
                  <h2 className="film-info__title t-preview-text secondary">
                    {film.Film_title}
                  </h2>
                </div>
                <p className="film-info__director body-text">{film.Director}</p>
                <div className="film-info__details body-text">
                  <p className="film-info__runtime">{film.Runtime}</p>
                  <p className="film-info__date">{film.Release_year}</p>
                </div>
                <div className="four_line_container body-text">
                  <p
                    className="film-info__synopsis p-preview-text body-text fw-skinny"
                    onClick={() => handleFilmClick(film)}
                  >
                    {film.Synopsis}
                  </p>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      <AnimatePresence>
        {selectedFilm && (
          <motion.aside
            className={`film-details-aside ${selectedFilm ? "visible" : ""}`}
            initial={{ translateY: "100%" }}
            animate={{
              translateY: "0%",
              opacity: "100%",
              transition: { duration: 0.75, ease: "easeOut" },
            }}
            exit={{
              translateY: "100%",
              // opacity: 0,
              transition: {
                duration: 0.5,
                ease: "easeIn",
              },
            }}
            drag="y"
            dragConstraints={{ top: 0, bottom: 0 }}
            dragElastic={0.7}
            onDragEnd={handleDragEnd}
          >
            <button
              className="secondary button_container"
              onClick={handleAsideClose}
            >
              <div className="drag-container">
                <div className="line_div_drag" />
              </div>
            </button>
            <h2 className="primary">{selectedFilm.Film_title}</h2>
            <p className="secondary">{selectedFilm.Director}</p>
            <div className="film-info__details secondary">
              <p>{selectedFilm.Runtime}</p>
              <p>{selectedFilm.Release_year}</p>
            </div>
            <p className="secondary fw-skinny">{selectedFilm.Synopsis}</p>
          </motion.aside>
        )}
      </AnimatePresence>
      <div className="flex-center selector-wrapper-padding">
        <button className="SelectorButtonNext button">Submit Rankings</button>
      </div>
    </div>
  );
}

export default Selector;
