from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import time
import make_film_list

# films watched url TEST
url_watched = 'https://letterboxd.com/brunardothegoat/list/testerwatchlist/'

# letterboxd list urls TEST
url_one = 'https://letterboxd.com/brunardothegoat/list/tester1/'
url_two = 'https://letterboxd.com/brunardothegoat/list/tester2/'
url_three = 'https://letterboxd.com/brunardothegoat/list/tester3/'

# scrape watched films
watched = make_film_list.get_watched_films(url_watched)
print('\n\nget_watched_films_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# scrape letterboxd lists
listOne, listTwo, listThree = make_film_list.get_lists(url_one, url_two, url_three, watched)
print('\n\nget_lists_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# get film options
the_films = make_film_list.get_options(listOne, listTwo, listThree)

def sensor():
    """ Function for test purposes. """
    print("\nScheduler is alive!")
    the_films = make_film_list.get_options(listOne, listTwo, listThree)
    make_film_list.print_films(the_films)
    print('\n\n\nget_options_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def two():
    """ Function for test purposes. """
    print("\nTWO :)!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=30)
sched.add_job(two,'interval',seconds=30)
sched.start()

app = Flask(__name__)
CORS(app)

@app.route("/film_dict")
def film_dict():
    # The film_list dictionary
    films = the_films
    return jsonify(films)


@app.route("/home")
def home():
    """ Function for test purposes. """
    output_film_dict = film_dict()
    return output_film_dict

if __name__ == "__main__":
    app.run()