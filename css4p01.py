# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:53 2024

@author: Katlego Molapo
"""

##CLEANING DATA

import pandas as pd

df = pd.read_csv('movie_dataset.csv')

df.dropna(inplace=True)

df= df.reset_index(drop = True)

df.drop_duplicates(inplace= True)



##QUESTION 1
max_rating_index = df['Rating'].idxmax()
title = df.at[max_rating_index, 'Title']
print("The most rated movie is", title)


##QUESTION 2
average_revenue = df['Revenue (Millions)'].mean()
print("The average revenue is",average_revenue)


##QUESTION 3
years_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_of_years_2015_2017 = years_2015_2017['Revenue (Millions)'].mean()
print("Average revenue from 2015 to 2017:", average_revenue_of_years_2015_2017)


##QUESTION 4
movies_2016 = df[df['Year'] == 2016]
number_of_movies_in_2016 = len(movies_2016)
print("Number of movies in 2016 is", number_of_movies_in_2016)


##QUESTION 5
movies_by_nolan = df [df["Director"]=="Christopher Nolan"]
number_of_movies_created_by_nolan = len(movies_by_nolan)
print("Number of movies created by Nolan", number_of_movies_created_by_nolan)


##QUESTION 6
rating_8 = df[df['Rating']>=8]
number_of_rating_8 = len(rating_8)
print("Movies with ratings of at least 8 is", number_of_rating_8)


##QUESTION 7
median_nolan = movies_by_nolan['Rating'].median()
print("The rating of movies by Nolan is", median_nolan)


##QUESTION 8
average_ratings_by_year = df.groupby('Year')['Rating'].mean()
year_highest_avg_rating = average_ratings_by_year.idxmax()
highest_avg_rating = average_ratings_by_year.max()
print("Year with the highest average rating is", highest_avg_rating)


##QUESTION 9
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100
print("Percentage increase in the number of movies between 2006 and 2016 is", percentage_increase)


##QUESTION 10
from collections import Counter
all_actors = df['Actors'].str.split(', ').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0]
print("Most common actor in all the movies is", most_common_actor)


##QUESTION 11
unique_genres = df['Genre'].str.split(', ').explode().nunique()
print("The number of unique genres in the dataset is",unique_genres)
