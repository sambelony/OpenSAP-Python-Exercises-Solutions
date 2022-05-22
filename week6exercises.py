# Import the random library and have a look at the function gauss() which gives back a random float number.
# Which parameters are required? Write a function gaussian_distribution() that returns a list of 1000 random
# numbers with a mean of 100 and a standard deviation of 10. Invoke this function.
# For the resulting list calculate and print the mean and the standard deviation using the respective functions
# from the statistics library.

import random
import statistics

def gaussian_distribution():
    random_list = [random.gauss(100, 10) for n in range(1000)]
    print(random_list)
    return random_list

global_random_list = gaussian_distribution()

print("Mean:", statistics.mean(global_random_list))
print("Standard Deviation:", statistics.stdev(global_random_list))


# The non-standard library py-sudoku offers the possibility to create your own sudokus.
# Follow the above link and have a look how to install and use the library.
# Install the library and create a new sudoku with a difficulty of 0.7 Display the sudoku and the solution of the sudoku.

from sudoku import Sudoku

puzzle = Sudoku(3).difficulty(0.7)
puzzle.show()

solution = puzzle.solve()
solution.show()


# In this assignment you are going to build a Python program to access the Apple iTunes Search Service.
# This service can be used to search information about musicians, albums, songs and so on.
# Using the following URL, a search for the term ramones and for the entity type album is performed:
# https://itunes.apple.com/search?term=ramones&entity=album
# The Requests library can be used to invoke the Apple iTunes Search Service.
# In order to perform a search, a GET request needs to be performed.
# This is done using the get() function of the Requests library.
# After that, the method json() of the Requests library can be used to map the response from JSON to the Python data types dict and list.
# Write a program that asks the user for a search term.
# Perform a search using the iTunes search service for the entity type album.
# The program should then print how many search results where returned.
# For each result print the artist name, the album name and track count.

import requests

r = requests.get(f"https://itunes.apple.com/search?term={input('Please enter a search term:')}&entity=album").json()

print(f"The search returned {r.get('resultCount')} results.")

for i in range(r.get('resultCount')):
    print(f"Artist: {r.get('results')[i].get('artistName')} - Album: {r.get('results')[i].get('collectionName')} - Track Count: {r.get('results')[i].get('trackCount')}")


# Using the library random create 10,000 random points inside the square.
# That means generate 10,000 random pairs of values for x and y.
# The random value must be between 0 and 1 in order for a point to be inside the square.
# For each point check if x² + y² is < 1. If this is the case, then the point is within the circle.
# Count the total number of points and the points which are in the circle. Use these numbers to calculate π.
# Finally compare your calculated value of π with the value of π found in the math library.
# Do this by printing the calculated value of π, the value from the math library as well as the difference.

import random
import math

random_x = [random.random() for n in range(10000)]
random_y = [random.random() for n in range(10000)]
count = 0
for i in range(len(random_x)):
    if (random_x[i]**2 + random_y[i]**2) < 1:
        count += 1
calc_p = 4*count/len(random_x)

print("Calculated value of π:", calc_p)
print("Value of π from math library:", math.pi)
print("Difference:", math.pi - calc_p)
