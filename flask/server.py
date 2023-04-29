import time
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
import make_film_list

# films watched url
url_watched = 'https://letterboxd.com/BrunardoTheGoat/films/'

# letterboxd list urls
url_one = 'https://letterboxd.com/brunardothegoat/list/check-out-this-filmmaker/'
url_two = 'https://letterboxd.com/brunardothegoat/list/on-my-radar/'
url_three = 'https://letterboxd.com/brunardothegoat/list/new-finds/'


# scrape watched films
watched = make_film_list.get_watched_films(url_watched)
print('\n\nget_watched_films_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# scrape letterboxd lists
listOne, listTwo, listThree = make_film_list.get_lists(url_one, url_two, url_three, watched)
print('\n\nget_lists_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# get film options
the_films = make_film_list.get_options(listOne, listTwo, listThree)

# print the film list
make_film_list.print_films(the_films)
print('\n\nget_options_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# Define the functions to schedule
def get_watched_films_job():
    global watched
    print("\nScheduler is alive!")
    watched = make_film_list.get_watched_films(url_watched)
    print('\n\n\nget_watched_films_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def get_lists_job():
    global listOne, listTwo, listThree
    print("\nScheduler is alive!")
    print(watched)
    listOne, listTwo, listThree = make_film_list.get_lists(url_one, url_two, url_three, watched)
    print('\n\n\nget_lists_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def get_options_job():
    global the_films
    print("\nScheduler is alive!")
    the_films = make_film_list.get_options(listOne, listTwo, listThree)
    make_film_list.print_films(the_films)
    print('\n\n\nget_options_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Schedule the functions
sched = BackgroundScheduler(daemon=True)
sched.add_job(get_watched_films_job, 'cron', hour=4)
sched.add_job(get_lists_job, 'cron', hour=4)
sched.add_job(get_options_job, 'interval', minutes=15)
sched.start()

app = Flask(__name__)
CORS(app)

@app.route("/film_dict")
def film_dict():
    # The film_list dictionary
    films = the_films
    return jsonify(films)


@app.route("/")
def home():
    output_film_dict = film_dict()
    return output_film_dict


if __name__ == "__main__":

    # Run the Flask app
    app.run(debug=True)