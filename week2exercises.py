# Below you find a code snippet to create a Python list containing the titles of all Star Wars movies. The list contains:
# A list containing the titles of the prequel trilogy: The Phantom Menace, Attack of the Clones, Revenge of the Sith
# A list containing the titles of the original trilogy: A New Hope, The Empire Strikes Back, Return of the Jedi,
# A list containing the titles of the sequel trilogy: The Force Awakens, The Last Jedi, The Rise of Skywalker

star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]
trilogy = int(input()) - 1
film = int(input()) - 1
print(star_wars_movies[trilogy][film])


# You are given the following list containing stock symbols, their current price as well as the absolute price change of the previous day:
# stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
# As you plan to take some of the profits, write a program that creates a list of all the stock symbols with a change of more than +5 percent.
# The list should be named sell_list. The list should only contain the stock symbol, not the price or the absolute change.
# Print the resulting list.

stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
sell_list = []
for s in stocks:
    if s[-1] > 5:
        sell_list.append(s[0])
print(sell_list)


# Write a program that lets the user input a two-dimensional matrix (Hint: you could use a list of lists to store the matrix).
# The program should first ask the user how many rows and columns the matrix should contain.
# Next, the program should ask the user for the elements of the matrix.
# Your program should read the values from the user row by row.
# If, for example, the matrix has the dimension 2 by 3, the values should be read as follows:
#     First row, first value
#     First row, second value
#     First row, third value
#     Second row, first value
#     Second row, second value
#     Second row, third value
# Finally, the program should calculate and print the sums of the values in each row.

row = int(input("Please enter the number of rows in the matrix:"))
column = int(input("Please enter the number of columns in the matrix:"))
matric = []
matrir = []
for r in range(row):
    for с in range(column):
        element = int(input("Value:"))
        matrir.append(element)
    matric.append(matrir)
    matrir = []
for rows in matric:
    print("Sum of row:" + str(sum(rows)))


# In this exercise you are going to simulate a sales and operations planning using the zero stock level strategy.
# Write a Python program that asks the user to enter the following data:
#     An initial stock level for a product
#     The number of month(s) to plan
#     The planned sales quantity for each month
# Based on this data, calculate the required production quantity as follows:
# If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
# If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

stock_level = int(input("Please enter an initial stock level:"))
num_of_month = int(input("Please enter the number of month to plan:"))
planned_sales = [int(input("Please enter the planned sales quantity:"))  for x in range(num_of_month)]
print("The resulting production quantities are:")
for plan in range(len(planned_sales)):
    if stock_level >= planned_sales[plan]:
        prod_quant = 0
        stock_level = stock_level - planned_sales[plan]
    else:
        prod_quant = abs(planned_sales[plan] - stock_level)
        stock_level = 0
    print("Production quantity month", plan + 1, "-", prod_quant)
