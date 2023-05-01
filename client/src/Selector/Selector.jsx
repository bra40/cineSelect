import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import FilmOption from "./FilmOption";
import FilmAside from "./FilmAside";
import SelectorSkeleton from "../Skeletons/SelectorSkeleton";
import "./selector.scss";

function Selector() {
  const [selectedFilm, setSelectedFilm] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [films, setFilms] = useState([]);

  const pollData = async (url, interval, maxAttempts) => {
    let attempts = 0;

    while (attempts < maxAttempts) {
      try {
        const result = await axios(url);
        return result.data;
      } catch (error) {
        console.error(error);
        await new Promise((resolve) => setTimeout(resolve, interval));
        attempts++;
      }
    }

    throw new Error(`Max attempts reached (${maxAttempts})`);
  };

  const fetchData = useCallback(async () => {
    try {
      const data = await pollData("http://localhost:5000/", 15000, 24);
      setFilms(data);
      setIsLoading(false);
    } catch (error) {
      console.error(error);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);


  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       setIsLoading(true);
  //       const result = await axios("http://localhost:5000/");
  //       setFilms(result.data);
  //       setIsLoading(false);
  //     } catch (error) {
  //       console.error(error);
  //     }
  //   };

  //   const delay = setTimeout(() => {
  //     fetchData();
  //   }, 60000); // wait for 1 minute (60,000 milliseconds) before making the axios call

  //   return () => {
  //     clearTimeout(delay);
  //   };
  // }, []);

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
      <div className="flex-center selector-wrapper-padding">
        <h3 className="secondary lowercase">click to rank</h3>
        <h2 className="primary capitalize text-center">
          user one’s preferences
        </h2>
      </div>
      <div className="selector-container">
        {[...Array(3)].map(
          (_, i) =>
            isLoading && (
              <div key={i} className={`film-section__${i + 1}`}>
                <div className={`line-div__${i + 1}`} />
                <SelectorSkeleton key={i} />
              </div>
            )
        )}
        {films.map((film, index) => (
          <div key={index} className={`film-section__${index + 1}`}>
            <div className={`line-div__${index + 1}`} />
            <FilmOption
              key={index}
              film={film}
              index={index}
              handleFilmClick={handleFilmClick}
            />
          </div>
        ))}
      </div>

      <FilmAside
        selectedFilm={selectedFilm}
        handleAsideClose={handleAsideClose}
        handleDragEnd={handleDragEnd}
      />

      <div className="flex-center selector-wrapper-padding">
        <button className="button">Submit Rankings</button>
      </div>
    </div>
  );
}

export default Selector;
