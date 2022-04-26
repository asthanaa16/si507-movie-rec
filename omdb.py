import json, requests, copy


BASE_URL = 'http://www.omdbapi.com/?apikey=5e0924db&'


genre_list = ['Action', 'Animation', 'Biopic','Comedy', 'Crime','Drama','Documentary','Fantasy','Historical','Horror','Romance','Science Fiction','Thriller','Musical','War']


#print(requests.get(BASE_URL+'t=Shrek').json())


