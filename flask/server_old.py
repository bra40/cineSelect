from flask import Flask, jsonify
# 6. Execute Operation

# # films watched url
# url_watched = 'https://letterboxd.com/BrunardoTheGoat/films/'

# # letterboxd list urls
# url_one = 'https://letterboxd.com/brunardothegoat/list/check-out-this-filmmaker/'
# url_two = 'https://letterboxd.com/brunardothegoat/list/on-my-radar/'
# url_three = 'https://letterboxd.com/brunardothegoat/list/new-finds/'
import schedule
import time
from flask_cors import CORS
import make_film_list


app = Flask(__name__)
CORS(app)


# films watched url TEST
url_watched = 'https://letterboxd.com/brunardothegoat/list/testerwatchlist/'

# letterboxd list urls TEST
url_one = 'https://letterboxd.com/brunardothegoat/list/tester1/'
url_two = 'https://letterboxd.com/brunardothegoat/list/tester2/'
url_three = 'https://letterboxd.com/brunardothegoat/list/tester3/'

# scrape watched films
watched = make_film_list.get_watched_films(url_watched)
print('get_watched_films_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# scrape letterboxd lists
listOne, listTwo, listThree = make_film_list.get_lists(url_one, url_two, url_three, watched)
print('get_lists_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# get film options
the_films = make_film_list.get_options(listOne, listTwo, listThree)

# print the film list
make_film_list.print_films(the_films)
print('get_options_OG: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Define the functions to schedule
def get_watched_films_job():
    watched = make_film_list.get_watched_films(url_watched)
    print('get_watched_films_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def get_lists_job():
    print(watched)
    listOne, listTwo, listThree = make_film_list.get_lists(url_one, url_two, url_three, watched)
    print('get_lists_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def get_options_job():
    the_films = make_film_list.get_options(listOne, listTwo, listThree)
    print('get_options_job: Completed at', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


@app.route("/film_dict")
def film_dict():
    # The film_list dictionary
    films = the_films

    return jsonify(films)

@app.route("/")
def home():
    output_film_dict = film_dict()
    return output_film_dict

if __name__ == "main":
    msg = "main"
    print(msg)
    app.run(debug=True)

    # Run the scheduled functions initially
    # Schedule the functions
    schedule.every().day.at("12:00").do(get_watched_films_job)
    schedule.every().day.at("12:00").do(get_lists_job)
    schedule.every(2).minutes.do(get_options_job)    

    # Start the scheduling loop
    while True:
        schedule.run_pending()
        time.sleep(1)