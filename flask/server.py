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

# my_list_url = "https://letterboxd.com/brunardothegoat/list/mexican-gold/"

# from bs4 import BeautifulSoup
# import requests
# from tqdm import tqdm
# import numpy as np
# import pandas as pd



# _domain = "https://letterboxd.com/"
# current_list = pd.DataFrame()

# def scrape_list(list_link):
#     """
#     Takes in a Letterboxd link and outputs a list of film title, release year, 
#     director, cast, average rating and letterboxd url
#     """
    
#     film_rows = []
#     film_rows.append(["Film_title", "Release_year", "Director", "Cast", "Personal_rating", "Average_rating","Letterboxd URL"])
    
#     while True:
#         list_page = requests.get(list_link)
        
#         # check to see page was downloaded correctly
#         if list_page.status_code != 200:
#             encounter_error("")

#         soup = BeautifulSoup(list_page.content, "html.parser")
#         # browser.get(following_url)
        
#         # grab the main film grid
#         table = soup.find("ul", class_="poster-list")
#         # print(table)
#         if table is None:
#             return None
        
#         films = table.find_all("li")
        
#         # films = table.find_all("li", class_="film-not-watched")
        
#         # iterate through films
#         for film in tqdm(films):
            
#             # print("films: " + film)
#             # finding the film name
#             panel = film.find("div").find("img")
#             film_name = panel["alt"]
            
#             # try to find the rating of a film if possible and converting to float
#             try:
#                 stars = film.find("span", class_="rating").get_text().strip()
#                 rating = transform_stars(stars)
#             except:
#                 rating = np.nan
            
#             # Obtaining release year, director, cast and average rating of the movie
#             film_card = film.find("div").get("data-target-link")
#             film_page = _domain + film_card
#             filmget = requests.get(film_page)
#             film_soup = BeautifulSoup(filmget.content, "html.parser")
            
#             release_year = film_soup.find("meta", attrs={"property":"og:title"}).attrs["content"][-5:-1]
#             director = film_soup.find("meta", attrs={"name":"twitter:data1"}).attrs["content"]
            
#             # try to find the cast, if not found insert a nan
#             try:
#                 cast = [ line.contents[0] for line in film_soup.find("div", attrs={"id":"tab-cast"}).find_all("a")]
                
#                 # remove all the "Show All..." tags if they are present
#                 cast = [i for i in cast if i != "Show All…"]
            
#             except:
#                 cast = np.nan
            
#             # try to find average rating, if not insert a nan
#             try:
#                 average_rating = float(film_soup.find("meta", attrs={"name":"twitter:data2"}).attrs["content"][:4])
#             except:
#                 average_rating = np.nan

#             film_rows.append([film_name, release_year, director, cast, rating, average_rating, _domain+film_card])
            
#         # check if there is another page of ratings
#         next_button = soup.find("a", class_="next")
#         if next_button is None:
#             break
#         else:
#             list_link = _domain + next_button["href"]
            
#     return film_rows

# def transform_stars(starstring):
#     """
#     Transforms star rating into float value
#     """
#     stars = {
#         "★": 1,
#         "★★": 2,
#         "★★★": 3,
#         "★★★★": 4,
#         "★★★★★": 5,
#         "½": 0.5,
#         "★½": 1.5,
#         "★★½": 2.5,
#         "★★★½": 3.5,
#         "★★★★½": 4.5
#     }
#     try:
#         return stars[starstring]
#     except:
#         return np.nan

#         # -------------------------------------

# import csv
# import pandas as pd
# from google.colab import files

# def list_to_csv(film_rows, list_name):
#     """
#     Takes in a list of filmrows outputted by the list_scraper()
#     and converts it to a CSV file
    
#     """
    
#     with open(f"{list_name}.csv", "w") as f:
#         write = csv.writer(f)
#         write.writerows(film_rows)

#     df = pd.read_csv(f"{list_name}.csv")
#     global current_list
#     current_list = df
#     # print(brunos_films.to_string())
#     df.to_csv(f"{list_name}.csv") 
#     # files.download(f"{list_name}.csv") 
        
#     return

#         # -------------------------------------

# # from list_scraper import *

# class List:
#     """
#     List to store data pertaining to a specific list
#     """
    
#     def __init__(self, list_name, link):
#         """
#         :param list_name: List name for data file (if applicable):
#         :param link: The link of the list
#         """
        
#         self.name = list_name
#         self.link = link
#         print("\nScraping list data...\n")
#         self.films = scrape_list(self.link)

#         # -------------------------------------

# """
# Letterboxd List scraper - main program
# """

# def main(my_list_url):
#     print("====================================================")
#     print("Welcome to the Letterboxd List scraper!")
#     print("Provided with an URL, this program outputs a CSV file") 
#     print("of movie title, release data and Letterboxd link.") 
#     print("Example url: https://letterboxd.com/.../list/short-films/).")
#     print("The program currently only supports lists and watchlists.")
#     print("Enter q or quit to exit the program.")
#     print("====================================================\n")
    
#     # Checking if URL is of a watchlist or of a list
#     while True:
#         # list_url = input("Enter the URL of the list you wish to scrape:")
#         list_url = my_list_url
#         print(list_url)
        
#         # exit option
#         if list_url == "q" or list_url == "quit":
#             exit()
            
#         # if a watchlist proceed this way
#         elif list_url.split("/")[-3] != "list":
#             try:
#                 list_name = list_url.split("/")[-2]
#                 username = list_url.split("/")[-3]
#                 current_list = List(list_name, list_url)
#                 break

#             except:
#                 print("That is not a valid URL, please try again.")
#                 continue
        
#         # if a list proceed this way
#         elif list_url.split("/")[-3] == "list":
#             try:
#                 list_name = list_url.split("/")[-2]
#                 current_list = List(list_name, list_url)
#                 break

#             except:
#                 print("That is not a valid URL, please try again.")
#                 continue
    
#     # writing to a CSV file
#     try:
#         csv_name = username + "_" + list_name
#         print(f"Writing to {csv_name}.csv.")
#         list_to_csv(current_list.films, csv_name)
          
#     except:
#         print(f"Writing to {list_name}.csv.")
#         list_to_csv(current_list.films, list_name)
    
#     print("Done!")

# def choose_three_films():
#     my_list_url = "https://letterboxd.com/brunardothegoat/films/"
#     main(my_list_url)
#     brunos_watched = current_list

#     my_list_url = "https://letterboxd.com/brunardothegoat/list/mexican-gold/"
#     main(my_list_url)
#     mexican_gold = current_list

#     my_list_url = "https://letterboxd.com/brunardothegoat/list/watch-soon/"
#     main(my_list_url)
#     watch_soon = current_list

#     my_list_url = "https://letterboxd.com/brunardothegoat/list/understanding-film-history/"
#     main(my_list_url)
#     understanding_film_history = current_list

#     listOne = pd.merge(mexican_gold, brunos_watched, on=["Film_title", "Release_year", "Director", "Cast", "Personal_rating", "Average_rating","Letterboxd URL"], how="outer", indicator=True
#                   ).query("_merge=="left_only"")
#     listOne = listOne.drop(["_merge",], axis=1)

#     listTwo = pd.merge(watch_soon, brunos_watched, on=["Film_title", "Release_year", "Director", "Cast", "Personal_rating", "Average_rating","Letterboxd URL"], how="outer", indicator=True
#                   ).query("_merge=="left_only"")
#     listTwo = listTwo.drop(["_merge",], axis=1)

#     listThree = pd.merge(understanding_film_history, brunos_watched, on=["Film_title", "Release_year", "Director", "Cast", "Personal_rating", "Average_rating","Letterboxd URL"], how="outer", indicator=True
#                   ).query("_merge=="left_only"")
#     listThree = listThree.drop(["_merge",], axis=1)

#     def choose_one():
#       chosenOne = listOne.sample()
#       chosenOne.reset_index(inplace = True, drop = True)
#       return chosenOne

#     def choose_two():
#       chosenTwo = listTwo.sample()
#       chosenTwo.reset_index(inplace = True, drop = True)
#       return chosenTwo

#     def choose_three():
#       chosenThree = listThree.sample()
#       chosenThree.reset_index(inplace = True, drop = True)
#       return chosenThree

#     one = choose_one()
#     two = choose_two()
#     three = choose_three()

#     while two.equals(one):
#       two = choose_two()

#     while two.equals(three):
#       three = choose_three()

#     films = pd.DataFrame([one.loc[0],two.loc[0],three.loc[0]])
#     films.reset_index(inplace=True, drop=True)

#     return films

@app.route("/")
def home():
    s = "taha_and_bruno_incorporated"
    s = film_dict()
    return s

if __name__ == "main":
    msg = "main"
    print(msg)
    app.run(debug=True)