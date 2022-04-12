from bs4 import BeautifulSoup
from urllib.request import urlopen

f = open("oscars-all-nominations.html")

html_text = f.read()

soup = BeautifulSoup(html_text, 'html.parser')
all_movies = soup.find_all('a', class_='nominations-link')

#print(len(all_movies))