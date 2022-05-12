# Implement a function named get_student_data().
# The function should do the following:
# Using input() it asks for name, first name and a student-id.
# The values are packed into a tuple.
# This tuple is returned from the function
# The function get_student_data() is then called in the program, the return value is assigned to a variable.
# Finally, output the variable using print().

def get_student_data():
    name = input("Name?")
    nachname = input("Nachname?")
    student_id = input("Stud id?")
    return (name, nachname, student_id)

print(get_student_data())


# Implement the function is_even(number) which gets an integer as input parameter and checks, if this input is even or not.
# is_even() will return the boolean value True if the value is even and False if the input is not even.
# Implement a for loop which iterates over the range(100).
# Within the for loop, the sequence-variable is checked with the function is_even().
# Depending on the return value, either x is even or x is not even is printed.

def is_even(number):
    return number % 2 == 0

for n in range(100):
    if is_even(n):
        print(n, "is even")
    else:
        print(n, "is not even")


# The stopping distance of a car can be calculated using the following rule of thumb:
# The stopping distance of the car is the sum of the reaction path and the brake distance
# The reaction path depends on the speed. It can be calculated by the following rule of thumb:
# The reaction path in meter is equal to the speed in km/h times 3/10.
# Example: Speed 50km/h –> reaction path 15m
# The brake distance depends as well on the speed.
# Again there is a rule of thumb which is: brake distance in m is equal to the speed in km/h divided by 10,
# the result has to be taken by the power of 2 - Example: Speed 50km/h –> (50 / 10)**2 = 25m
# The stopping distance for a car with a speed of 50km/h is 15m + 25m = 40m
# Implement the following functions to calculate the stopping distance
# function reaction_path() which gets the speed in km/h as input, calculates the reaction path according
# to the above rule of thumb and returns the path in m
# function brake_distance() which gets the speed in km/h as input, calculates the brake distance according
# to the above rule of thumb and returns the distance in m
# function stopping_distance() which gets the speed in km/h as input, calls the above functions,
# adds their return values and returns this sum
# Get a speed in km/h as input and output the stopping distance in m.

def reaction_path(speed):
    return speed*3/10

def brake_distance(speed):
    return (speed/10)**2

def stopping_distance(speed):
    return reaction_path(speed) + brake_distance(speed)

print(stopping_distance(50))
