from oscars_db import movies
from omdb import BASE_URL, genre_list
import json, requests, copy
from final_proj_tree import BinaryTree,TreeNode
from movie_rec import json_movies
from PIL import Image
from io import BytesIO
import pandas as pd


poster_url = 'http://img.omdbapi.com/?apikey=5e0924db&'

affirm = ['yes','ya','yeah','y','YES','Y']
neg = ['no','NO','n','N','nah']
movie_tree = BinaryTree(json_movies)
print("Welcome to the Oscars movie recommendation system! We have compliled every movie ever nominated for an Oscar. Answer a few questions about your movie preferences, and we will give you some recs!")
awards_won = input("Do you only want movies that have won an oscar?")
winning_movies = []
losing_movies = []

for movie in json_movies:
        if movie['Awards'][0] == "Won":
            winning_movies.append(movie)
        else:
            losing_movies.append(movie)

if awards_won in affirm:
    movie_tree.insertRight(winning_movies)
    movie_tree.insertLeft(losing_movies)

elif awards_won in neg:
    movie_tree.insertRight(losing_movies)
    movie_tree.insertLeft(winning_movies)

language = input("Do you only want English language movies?")
for movie in winning_movies:
    if "English" or "None" not in movie['Language']:
        losing_movies.append(movie)
        winning_movies.pop(movie)
for movie in losing_movies:
    if "English" or "None" not in movie['Language']:
        winning_movies.append(movie)
        losing_movies.pop(movie)

if awards_won in affirm:
    movie_tree.insertRight(winning_movies)
    movie_tree.insertLeft(losing_movies)

elif awards_won in neg:
    movie_tree.insertRight(losing_movies)
    movie_tree.insertLeft(winning_movies)

ratings_site = input("Do you want ratings from Rotten Tomatoes, IMDb, or both? Enter R for rotten tomatoes, I for IMDB, or B for both.")
ratings = input("Do you want a movie with an above rating? (As of 2020 the average rating for Rotten Tomatoes is 62 and 7.0 for IMDb)")

if ratings in affirm:
    if ratings_site == 'R':
        for movie in winning_movies:
            if int(movie['Ratings'][1]['Value'][:2]) <= 62:
                losing_movies.append(movie)
                winning_movies.pop(movie)
    if ratings_site == 'I':
        if float(movie['Ratings'][0]['Value'][:2]) <= 7.0:
                losing_movies.append(movie)
                winning_movies.pop(movie)
    else:
        if ((float(movie['Ratings'][0]['Value'][:2]) <= 7.0) and (int(movie['Ratings'][1]['Value'][:2]) <= 62)):
            losing_movies.append(movie)
            winning_movies.pop(movie)

elif ratings in neg:
    if ratings_site == 'R':
        for movie in winning_movies:
            if int(movie['Ratings'][1]['Value'][:2]) > 62:
                losing_movies.append(movie)
                winning_movies.pop(movie)
    if ratings_site == 'I':
        if float(movie['Ratings'][0]['Value'][:2]) > 7.0:
                losing_movies.append(movie)
                winning_movies.pop(movie)
    else:
        if ((float(movie['Ratings'][0]['Value'][:2]) > 7.0) and (int(movie['Ratings'][1]['Value'][:2]) <= 62)):
            losing_movies.append(movie)
            winning_movies.pop(movie)
movie_tree.insertRight(winning_movies)
movie_tree.insertLeft(losing_movies)

genre = input("Please enter your genre preference (only enter one genre). If you do not have one please enter none")

if genre != "none" or genre != "None":
    for movie in winning_movies:
        if genre.lower() not in movie['Genre'].lower():
            losing_movies.append(movie)
            winning_movies.pop(movie)

best_choices = []
movie_tree.insertRight(winning_movies)
movie_tree.insertLeft(losing_movies)

director = input("Do you have a prefered director? Keep in mind your favorite director my not have made a movie that meets the other requirements you specified! Enter none if you have no preference.")
if director != "none" or genre != "None":
    for movie in winning_movies:
        if director.lower() in movie['Director'].lower():
            best_choices.append(movie)

movie_tree.insertRight(best_choices)
movie_tree.insertLeft(winning_movies)

actor = input("Do you have a favorite actor? Keep in mind your favorite actor my not have starred in a movie that meets the other requirements you specified! Enter none if you have no preference.")
if actor != "none" or genre != "None":
    for movie in winning_movies:
        if actor.lower() in movie['Actors'].lower():
            best_choices.append(movie)

movie_tree.insertRight(best_choices)
movie_tree.insertLeft(winning_movies)

writer = input("Do you have a favorite screen writer? Keep in mind your favorite screen writer my not have starred in a movie that meets the other requirements you specified! Enter none if you have no preference.")
if writer != "none" or genre != "None":
    for movie in winning_movies:
        if writer.lower() in movie['Writer'].lower():
            best_choices.append(movie)

movie_tree.insertRight(best_choices)
movie_tree.insertLeft(winning_movies)

rated = input("Do you want to exclude movies with a PG-13 or higher rating?")
if rated in affirm:
    for movie in winning_movies:
        if movie['Rated'] != "PG" or movie['Rated'] != "G":
            winning_movies.pop(movie)
            if movie in best_choices:
                best_choices.pop(movie)

movie_tree.insertRight(best_choices)
movie_tree.insertLeft(winning_movies)

#data presentaion 1
if len(best_choices) > 0:
    print("Your top choice(s):")
    for movie in best_choices:
        print(movie['Title'])

for movie in winning_movies:
        print(movie['Title'])

#data presentaion 2
if len(best_choices) > 0:
    for movie in best_choices:
        print(movie['Title'],movie['Plot'])
        if movie['DVD'] != 'N/A':
            print("This is available on DVD!!")

for movie in winning_movies:
    print(movie['Title'],movie['Plot'])
    if movie['DVD'] != 'N/A':
        print("This is available on DVD!!")


#data presentation 3
if len(best_choices) > 0:
    for movie in best_choices:
        print(movie['Title'])
        im = Image.open(requests.get(movie['Poster'], stream=True).raw)
        print(movie['Plot'])

for movie in winning_movies:
    print(movie['Title'])
    im = Image.open(requests.get(movie['Poster'], stream=True).raw)
    print(movie['Plot'])

#data presentaion 4
if len(best_choices) > 0:
    print("These movies are your ideal matches! They fit your genre,ratings, awards, director, writer, and actor requirements the best!")
    print("Compare your movie recs to what you entered for your preferences!")
    df = pd.DataFrame(best_choices)
    print(df)
    print(ratings,genre,director,writer,actor)

print("These movies meet most, but not all of your requirements! Check them out!")
movie_df = pd.DataFrame(winning_movies)

print("Thanks for using the oscars movie recommender! Comeback next year, so you can see which nominees are a must watch for you!")


