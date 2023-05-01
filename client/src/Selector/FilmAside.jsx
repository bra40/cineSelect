import { AnimatePresence, motion } from "framer-motion";

const FilmAside = ({ selectedFilm, handleAsideClose, handleDragEnd }) => {
  return (
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
              <div className="line-div__drag" />
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
  );
};

export default FilmAside;
