import json, requests, copy

BASE_URL = 'http://www.omdbapi.com/?apikey=4697b61d&'



def get_omdb_resource(url, params=None, timeout=10):
    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


genre_list = ['Action', 'Animation', 'Biopic','Comedy', 'Crime','Drama','Documentary','Fantasy','Historical','Horror','Romance','Science Fiction','Thriller','Musical','War']


