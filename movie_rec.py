from matplotlib.font_manager import json_load
from oscars_db import movies
from omdb import BASE_URL
import json, requests, copy



#STRUCTURE: requests.get(BASE_URL+'t='+movies[0][0]+'&y='+movie[0][1])
json_movies = []
for movie in movies:
    movie_info = requests.get(BASE_URL + 't=' + movie[0] + '&y=' + movie[1]).json()
    json_movies.append(movie_info)

#print(json_movies[0])

f = open('movies.json','w')
for film in json_movies:
    cached = json.dumps(film)
    f.write(cached)
f.close()
