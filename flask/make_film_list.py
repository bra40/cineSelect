# 1. LetterBoxd Scraper

from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import numpy as np
import pandas as pd

_domain = 'https://letterboxd.com/'
current_list = pd.DataFrame()

def scrape_list(list_link):
    """
    Takes in a Letterboxd link and outputs a list of film title, release year, 
    director, cast, average rating and letterboxd url
    """
    
    film_rows = []
    film_rows.append(['Film_title', 'Release_year', 'Director', 'Cast', 'Personal_rating', 'Average_rating','Letterboxd URL'])
    
    while True:
        list_page = requests.get(list_link)
        
        # check to see page was downloaded correctly
        if list_page.status_code != 200:
            encounter_error("")

        soup = BeautifulSoup(list_page.content, 'html.parser')
        # browser.get(following_url)
        
        # grab the main film grid
        table = soup.find('ul', class_='poster-list')
        # print(table)
        if table is None:
            return None
        
        films = table.find_all('li')
        
        # films = table.find_all('li', class_='film-not-watched')
        
        # iterate through films
        for film in tqdm(films):
            
            # print("films: " + film)
            # finding the film name
            panel = film.find('div').find('img')
            film_name = panel['alt']
            
            # try to find the rating of a film if possible and converting to float
            try:
                stars = film.find('span', class_='rating').get_text().strip()
                rating = transform_stars(stars)
            except:
                rating = np.nan
            
            # Obtaining release year, director, cast and average rating of the movie
            film_card = film.find('div').get('data-target-link')
            film_page = _domain + film_card
            filmget = requests.get(film_page)
            film_soup = BeautifulSoup(filmget.content, 'html.parser')
            
            release_year = film_soup.find('meta', attrs={'property':'og:title'}).attrs['content'][-5:-1]
            director = film_soup.find('meta', attrs={'name':'twitter:data1'}).attrs['content']
            
            # try to find the cast, if not found insert a nan
            try:
                cast = [ line.contents[0] for line in film_soup.find('div', attrs={'id':'tab-cast'}).find_all('a')]
                
                # remove all the 'Show All...' tags if they are present
                cast = [i for i in cast if i != 'Show All…']
            
            except:
                cast = np.nan
            
            # try to find average rating, if not insert a nan
            try:
                average_rating = float(film_soup.find('meta', attrs={'name':'twitter:data2'}).attrs['content'][:4])
            except:
                average_rating = np.nan

            film_rows.append([film_name, release_year, director, cast, rating, average_rating, _domain+film_card])
            
        # check if there is another page of ratings
        next_button = soup.find('a', class_='next')
        if next_button is None:
            break
        else:
            list_link = _domain + next_button['href']
            
    return film_rows

def transform_stars(starstring):
    """
    Transforms star rating into float value
    """
    stars = {
        "★": 1,
        "★★": 2,
        "★★★": 3,
        "★★★★": 4,
        "★★★★★": 5,
        "½": 0.5,
        "★½": 1.5,
        "★★½": 2.5,
        "★★★½": 3.5,
        "★★★★½": 4.5
    }
    try:
        return stars[starstring]
    except:
        return np.nan

        # -------------------------------------

import csv
import pandas as pd

def list_to_csv(film_rows, list_name):
    """
    Takes in a list of filmrows outputted by the list_scraper()
    and converts it to a CSV file
    
    """
    
    with open(f'{list_name}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(film_rows)

    df = pd.read_csv(f'{list_name}.csv')
    global current_list
    current_list = df
    df.to_csv(f'{list_name}.csv') 
        
    return

        # -------------------------------------

# from list_scraper import *

class List:
    """
    List to store data pertaining to a specific list
    """
    
    def __init__(self, list_name, link):
        """
        :param list_name: List name for data file (if applicable):
        :param link: The link of the list
        """
        
        self.name = list_name
        self.link = link
        self.films = scrape_list(self.link)

        # -------------------------------------

'''
Letterboxd List scraper - main program
'''

def scrape_list_url(my_list_url):
    
    # Checking if URL is of a watchlist or of a list
    while True:
        # list_url = input('Enter the URL of the list you wish to scrape:')
        list_url = my_list_url
        print(list_url)
        
        # exit option
        if list_url == 'q' or list_url == 'quit':
            exit()
            
        # if a watchlist proceed this way
        elif list_url.split('/')[-3] != 'list':
            try:
                list_name = list_url.split('/')[-2]
                username = list_url.split('/')[-3]
                current_list = List(list_name, list_url)
                break

            except:
                print('That is not a valid URL, please try again.')
                continue
        
        # if a list proceed this way
        elif list_url.split('/')[-3] == 'list':
            try:
                list_name = list_url.split('/')[-2]
                current_list = List(list_name, list_url)
                break

            except:
                print('That is not a valid URL, please try again.')
                continue
    
    # writing to a CSV file
    try:
        csv_name = username + '_' + list_name
        print(f'Writing to {csv_name}.csv.')
        list_to_csv(current_list.films, csv_name)
          
    except:
        print(f'Writing to {list_name}.csv.')
        list_to_csv(current_list.films, list_name)
    
    print('Completed! :)')

# 2. HELPER FUNCTIONS
    
def get_tmdb_movie_id(api_key, query, year=None, director=None):
  """
  Searches for a movie by its title and returns the TMDB movie id and URL.
  
  :param api_key: str
      TMDB API key
  :param query: str
      Movie title to search for
  :param year: int, optional
      Release year of the movie
  :param director: str, optional
      Director of the movie
  :return: tuple of (int, str)
      TMDB movie id and URL
  """
  url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
  if year:
      url += f'&year={year}'
  response = requests.get(url)
  data = response.json()
  
  if director:
      for result in data['results']:
          if 'crew' in result:
              for crew_member in result['crew']:
                  if crew_member['job'] == 'Director' and crew_member['name'] == director:
                      return result['id'], f'https://www.themoviedb.org/movie/{result["id"]}'
          else:
              movie_id = result['id']
              url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
              response = requests.get(url)
              data = response.json()
              for crew_member in data['crew']:
                  if crew_member['job'] == 'Director' and crew_member['name'] == director:
                      return movie_id, f'https://www.themoviedb.org/movie/{movie_id}'
  
  return data['results'][0]['id'], f'https://www.themoviedb.org/movie/{data["results"][0]["id"]}'


def get_poster_url(title, year=None, director=None):
  """
  Searches for a movie by its title and returns the poster URL.
  
  :param title: str
      Movie title to search for
  :param year: int, optional
      Release year of the movie
  :param director: str, optional
      Director of the movie
  :return: str
      Poster URL
  """
  api_key = '6b17a09aed846d2e8d5f46e555aabb7a'
  movie_id = get_tmdb_movie_id(api_key, title, year, director)[0]
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
  response = requests.get(url)
  data = response.json()
  return f'https://image.tmdb.org/t/p/w500{data["poster_path"]}'

def get_backdrop_url(title, year=None, director=None):
  """
  Searches for a movie by its title and returns the poster URL.
  
  :param title: str
      Movie title to search for
  :param year: int, optional
      Release year of the movie
  :param director: str, optional
      Director of the movie
  :return: str
      Poster URL
  """
  api_key = '6b17a09aed846d2e8d5f46e555aabb7a'
  movie_id = get_tmdb_movie_id(api_key, title, year, director)[0]
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
  response = requests.get(url)
  data = response.json()
  return f'https://image.tmdb.org/t/p/w500{data["backdrop_path"]}'

def get_synopsis(title, year=None, director=None):
    """
    Searches for a movie by its title and returns the synopsis.
    
    :param title: str
        Movie title to search for
    :param year: int, optional
        Release year of the movie
    :param director: str, optional
        Director of the movie
    :return: str
        Synopsis
    """
    api_key = '6b17a09aed846d2e8d5f46e555aabb7a'
    movie_id = get_tmdb_movie_id(api_key, title, year, director)[0]
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['overview']

def format_duration(minutes):
  if minutes is None:
      return "N/A"
  hours, remainder = divmod(minutes, 60)
  if hours == 0:
      return f"{remainder}m"
  else:
      return f"{hours}h {remainder}m"

def get_movie_runtime(title, year=None, director=None):
  """
  Retrieves the runtime of a movie from its movie_id using the TMDB API.
  
  :param api_key: str
      Your TMDB API key
  :param movie_id: int
      The unique identifier for the movie on TMDB
  :return: str
      The formatted runtime of the movie
  """
  api_key = '6b17a09aed846d2e8d5f46e555aabb7a'
  movie_id = get_tmdb_movie_id(api_key, title, year, director)[0]
  url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
  response = requests.get(url)
  data = response.json()
  runtime = data['runtime']
  formatted_runtime = format_duration(runtime)
  return formatted_runtime

def print_films(film_list):
  for film in film_list:
    title = film['Film_title']
    director = film['Director']
    year = film['Release_year']
    runtime = film['Runtime']
    print(f'{title} was directed by {director} in {year}. ({runtime})')

# 3. Watchlist
def get_watched_films(url_watched):
    # Choose and scrape watchlist
    my_list_url = url_watched
    scrape_list_url(my_list_url)
    watched = current_list
    return watched

#4. Get Lists
def get_lists(url_one, url_two, url_three, watched):
    # Choose Lists to Scrape
    my_list_url = url_one
    scrape_list_url(my_list_url)
    list_one = current_list

    my_list_url = url_two
    scrape_list_url(my_list_url)
    list_two = current_list

    my_list_url = url_three
    scrape_list_url(my_list_url)
    list_three = current_list

    # Define the list of columns to drop then drop
    columns_to_drop = ['Cast', 'Personal_rating', 'Average_rating']

    list_one = list_one.drop(columns=columns_to_drop)
    list_two = list_two.drop(columns=columns_to_drop)
    list_three = list_three.drop(columns=columns_to_drop)

    # Only keep unwatched rows
    merged_df = pd.merge(list_one, watched, on=['Film_title', 'Director', 'Release_year','Letterboxd URL'], how='outer', indicator=True)
    result = merged_df[merged_df['_merge'] == 'left_only']
    listOne = result.drop(columns=['_merge'])

    merged_df = pd.merge(list_two, watched, on=['Film_title', 'Director', 'Release_year','Letterboxd URL'], how='outer', indicator=True)
    result = merged_df[merged_df['_merge'] == 'left_only']
    listTwo = result.drop(columns=['_merge'])

    merged_df = pd.merge(list_three, watched, on=['Film_title', 'Director', 'Release_year','Letterboxd URL'], how='outer', indicator=True)
    result = merged_df[merged_df['_merge'] == 'left_only']
    listThree = result.drop(columns=['_merge'])
    
    return (listOne, listTwo, listThree)

#5. Get Options
def get_options(listOne, listTwo, listThree):
    # no unwatched rows
    if listOne.empty and listTwo.empty and listThree.empty:
      raise ValueError("There must be unseen films in the list")

    # Choose a sample
    def choose_one():
      if listOne.empty:
        return choose_two()
      else:
        chosenOne = listOne.sample()
        chosenOne.reset_index(inplace = True, drop = True)
        return chosenOne

    def choose_two():
      if listTwo.empty:
        return choose_three()
      else:
        chosenTwo = listTwo.sample()
        chosenTwo.reset_index(inplace = True, drop = True)
        return chosenTwo

    def choose_three():
      if listThree.empty:
        return choose_one()
      else:
        chosenThree = listThree.sample()
        chosenThree.reset_index(inplace = True, drop = True)
        return chosenThree

    one = choose_one()
    two = choose_two()
    three = choose_three()

    # Have distinct choices
    while two['Film_title'].equals(one['Film_title']) or two['Film_title'].equals(three['Film_title']) or one['Film_title'].equals(three['Film_title']):
      if two['Film_title'].equals(one['Film_title']):
          two = choose_two()
      if two['Film_title'].equals(three['Film_title']):
          three = choose_three()
      if one['Film_title'].equals(three['Film_title']):
          three = choose_three()

    # Create a DataFrame from the first row of the one, two, and three DataFrames
    films = pd.DataFrame([one.loc[0],two.loc[0],three.loc[0]])

    # Reset the index of the films DataFrame
    films.reset_index(inplace=True, drop=True)
    film_list = films.to_dict(orient='records')

    # Iterate over each film in the film_list
    for film in film_list:
      film_title = film.get('Film_title')
      film_year = film.get('Release_year')
      film_director = film.get('Director')
      film['Poster_url'] = get_poster_url(film_title, film_year, film_director)
      film['Backdrop_url'] = get_backdrop_url(film_title, film_year, film_director)
      film['Synopsis'] = get_synopsis(film_title, film_year, film_director)
      film['Runtime'] = get_movie_runtime(film_title, film_year, film_director)
      del film['Cast']
      del film['Personal_rating']
      del film['Average_rating']

    # Return list of dictionaries
    return film_list