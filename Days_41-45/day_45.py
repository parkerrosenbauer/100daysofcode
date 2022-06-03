# Day 45 of 100 Days of Code Challenge
# Creating a text file of top 100 movies put together by Empire

import requests
from bs4 import BeautifulSoup

r = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_movies = r.text

soup = BeautifulSoup(empire_movies, "html.parser")

movie_titles = [movie.text for movie in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()

with open(file="top100.txt", mode="w", encoding='utf-8') as file:
    for title in movie_titles:
        file.write(title + '\n')
