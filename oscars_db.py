from bs4 import BeautifulSoup as bs
import requests
import urllib
import re
import pandas as pd
import os

oscars_base_url = 'https://letterboxd.com/nevertooearlymp/list/every-film-ever-nominated-for-an-academy/detail/page/'
#page/number/
movies = []
for page in range(1,52):
    req = requests.get(oscars_base_url + str(page) + '/')
    soup = bs(req.text,'html.parser')
    containers = soup.find_all("li",{"film-detail"})
    for i in containers:
        tup = (i.h2.a.text,i.small.a.text)
        movies.append(tup)


#print(movies[:3])




#print(type(movies))
#print(len(movies))
#print(movies[-1])
#print(movies[0])
