from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/film_dict")
def film_dict():
    films = [{'Film_title': 'Syndromes and a Century',
  'Release_year': 2006,
  'Director': 'Apichatpong Weerasethakul',
  'Average_rating': 3.98,
  'Letterboxd URL': 'https://letterboxd.com//film/syndromes-and-a-century/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/1XUMd93PRMUkCtE2NWn0zQb1NC6.jpg',
  'Synopsis': 'A story about director Apichatpong Weerasethakul’s parents who were both doctors, and his memories of growing up in a hospital environment.'},
 {'Film_title': 'The White Ribbon',
  'Release_year': 2009,
  'Director': 'Michael Haneke',
  'Average_rating': 4.07,
  'Letterboxd URL': 'https://letterboxd.com//film/the-white-ribbon/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/54dlnGDexrwAFlDb8HWKfmmX4LB.jpg',
  'Synopsis': 'Strange events happen in a small village in the north of Germany during the years just before World War I, which seem to be ritual punishment. The abused and suppressed children of the villagers seem to be at the heart of this mystery.'},
 {'Film_title': "Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan",
  'Release_year': 2017,
  'Director': 'Hong Sang-soo',
  'Average_rating': 3.39,
  'Letterboxd URL': 'https://letterboxd.com//film/claires-camera/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/n12X1HWLOLQXmh781WvG8McLuDI.jpg',
  'Synopsis': "Claire, a school teacher with a camera is on her first visit to Cannes. She happens upon a film sales assistant, Manhee, recently laid off after a one-night stand with a film director. Together, this unlikely pair become detectives of sorts, as they wander around the seaside resort town, working to better understand the circumstances of Manhee's firing."}]

    return jsonify(films)

@app.route("/")
def home():
    s = film_dict()
    return s

if __name__ == "main":
    msg = "main"
    print(msg)
    app.run(debug=True)