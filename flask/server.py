from flask import Flask, jsonify
from flask_cors import CORS
import make_film_list


app = Flask(__name__)
CORS(app)

the_films = make_film_list.get_films()

for film in the_films:
  title = film['Film_title']
  director = film['Director']
  year = film['Release_year']
  runtime = film['Runtime']
  print(f'{title} was directed by {director} in {year}. ({runtime})')



@app.route("/film_dict")
def film_dict():
    # Call the make_list function to generate the film_list dictionary
    films = the_films
    print(films)
#     films = [{
#   'Film_title': 'Timecode',
#   'Release_year': 2000,
#   'Director': 'Mike Figgis',
#   'Average_rating': 2.9,
#   'Letterboxd URL': 'https://letterboxd.com//film/timecode/',
#   'Poster_url': 'https://image.tmdb.org/t/p/w500/ptGDBAMfDOxr49RSTgMClxPiHjb.jpg',
#   'Synopsis': "A production company begins casting for its next feature, and an up-and-coming actress named Rose tries to manipulate her filmmaker boyfriend, Alex, into giving her a screen test. Alex's wife, Emma, knows about the affair and is considering divorce, while Rose's girlfriend secretly spies on her and attempts to sabotage the relationship. The four storylines in the film were each shot in one take and are shown simultaneously, each taking up a quarter of the screen.",
#   'Runtime': '1h 37m'},
#  {'Film_title': 'Caché',
#   'Release_year': 2005,
#   'Director': 'Michael Haneke',
#   'Average_rating': 3.95,
#   'Letterboxd URL': 'https://letterboxd.com//film/cache/',
#   'Poster_url': 'https://image.tmdb.org/t/p/w500/fnuAk6Or34FLYQDnh7Et51UvSXK.jpg',
#   'Synopsis': 'A married couple is terrorized by a series of videotapes planted on their front porch.',
#   'Runtime': '1h 57m'},
#  {'Film_title': 'The Man Who Shot Liberty Valance',
#   'Release_year': 1962,
#   'Director': 'John Ford',
#   'Average_rating': 4.15,
#   'Letterboxd URL': 'https://letterboxd.com//film/the-man-who-shot-liberty-valance/',
#   'Poster_url': 'https://image.tmdb.org/t/p/w500/4C1R0LEivLjbv3swAzJfzh0tzXl.jpg',
#   'Synopsis': 'A senator, who became famous for killing a notorious outlaw, returns for the funeral of an old friend and tells the truth about his deed.',
#   'Runtime': '2h 3m'
#   }]

    return jsonify(films)

@app.route("/")
def home():
    s = film_dict()
    return s

if __name__ == "main":
    msg = "main"
    print(msg)
    app.run(debug=True)