# The file numbers.txt contains random integer numbers.
# There is exactly one number per line. Read the file and output the three biggest numbers

with open("numbers.txt", "r") as file:
    list_of_ints = [int(line.strip()) for line in file]
list_of_ints.sort()
print(list_of_ints[-1])
print(list_of_ints[-2])
print(list_of_ints[-3])


# The file numbers.txt contains numbers. (Actually, the same numbers from the last exercise.)
# There is exactly one number per line. Read the numbers from the file and write only the even numbers into a new file named even_numbers.txt.
# Again, there should be one number per line.
# The order of the numbers shall be unchanged. To indicate that the program is finished, print the following output: “List of even numbers created!”

with open("numbers.txt", "r") as file:
    list_of_ints = [int(line.strip()) for line in file]
with open("even_numbers.txt", "w") as new_file:
    for num in list_of_ints:
        if num % 2 == 0:
            new_file.write(str(num) + "\n")
print("List of even numbers created!")


# The file invoice_data.txt contains raw data for an invoice.
# More precisely, each line contains
#
# the name of an item
# how many items are bought
# the unit price of the item
# The three values are separated by a single whitespace.
# Prepare a beautified output of the file which contains
#
# the name of the item formatted with 15 characters
# the number of units with 3 digits
# the price per item with 7 digits, 2 digits after the decimal point
# the total price (number of items * price per item) with 8 digits in total,
# 2 digits after the decimal point

with open("invoice_data.txt", "r") as file:
    list_tuples = [line.split() for line in file]
for item in list_tuples:
    print(f"{item[0]:15s}{int(item[1]):3d}{float(item[2]):7.2f}{(float(item[1])*float(item[2])):8.2f}")
