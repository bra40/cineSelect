from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/film_dict")
def film_dict():
    films = [
        {'Film_title': 'We Are the Nobles',
  'Release_year': 2013,
  'Director': 'Gary Alazraki',
  'Average_rating': 3.46,
  'Letterboxd URL': 'https://letterboxd.com//film/we-are-the-nobles/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/wsj9TvkL6Uh9leY08nuyE4OhOXW.jpg',
  'Synopsis': 'Tells the "riches to rags" story of the Nobles, three upper-class twenty-somethings that appear to have no limits to their checkbooks, and no direction in their lives. Until one day, their father tries to teach them a lesson by staging a financial scandal that forces the whole family to escape to an old house in the poor side of town, and leads the "kids" to do what they haven\'t done before: get jobs.'},
 {'Film_title': 'RRR',
  'Release_year': 2022,
  'Director': 'S. S. Rajamouli',
  'Average_rating': 4.17,
  'Letterboxd URL': 'https://letterboxd.com//film/rrr/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/nEufeZlyAOLqO2brrs0yeF1lgXO.jpg',
  'Synopsis': "A fictional history of two legendary revolutionaries' journey away from home before they began fighting for their country in the 1920s."},
 {'Film_title': '66 Scenes from America',
  'Release_year': 1982,
  'Director': 'Jørgen Leth',
  'Average_rating': 3.56,
  'Letterboxd URL': 'https://letterboxd.com//film/66-scenes-from-america/',
  'Poster_url': 'https://image.tmdb.org/t/p/w500/eVXGdi27vR46ecBZyvKoRT1AP7S.jpg',
  'Synopsis': 'As a visual narrative it is reminiscent of a pile of postcards from a journey, which indeed is what the film is. It consists of a series of lengthy shots of a tableau nature, each appearing to be a more or less random cross section of American reality, but which in total invoke a highly emblematic picture of the USA.'},
  ]

    return jsonify(films)

@app.route("/")
def home():
    s = film_dict()
    return s

if __name__ == "main":
    msg = "main"
    print(msg)
    app.run(debug=True)