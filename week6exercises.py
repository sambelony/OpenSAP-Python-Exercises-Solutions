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
