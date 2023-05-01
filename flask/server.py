import time
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
# from flask_socketio import SocketIO, emit
from flask import Flask, jsonify, render_template
import make_film_list

testing = True
testing = not testing

if testing:
    url_watched = 'https://letterboxd.com/brunardothegoat/list/testerwatchlist/'
    url_one = 'https://letterboxd.com/brunardothegoat/list/tester1/'
    url_two = 'https://letterboxd.com/brunardothegoat/list/tester2/'
    url_three = 'https://letterboxd.com/brunardothegoat/list/tester3/'
else:
    url_watched = 'https://letterboxd.com/BrunardoTheGoat/films/'
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
# the_films = get_options_job()

# print the film list
make_film_list.print_films(the_films)
print('\n\nget_options_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

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

# @socketio.on('get_options')
def get_options_job():
    global the_films
    print("\nScheduler is alive!")
    the_films = make_film_list.get_options(listOne, listTwo, listThree)
    make_film_list.print_films(the_films)
    print('\n\n\nget_options_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # emit('films-up__reload')

# Schedule the functions
sched = BackgroundScheduler(daemon=True)
sched.add_job(get_watched_films_job, 'cron', hour=4)
sched.add_job(get_lists_job, 'cron', hour=4)
sched.add_job(get_options_job, 'interval', minutes=15)
sched.start()

# @app.route('/message', methods=['GET'])
# def send_message():
#     message = {'content': 'Hello, world!'}
#     return render_template('index.html')

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