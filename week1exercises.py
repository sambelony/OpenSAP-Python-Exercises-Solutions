# Write a Python program that asks the user to enter:
#     A name
#     A start city
#     A destination city and
#     A means of transportation
# The program should then print that the name wants to travel from start to destination by means of transportation.

name = input("Name")
start = input("Start")
destination = input("Destination")
means_of_transportation = input("Means")
print(name,"wants to travel from",start, "to", destination, "by", means_of_transportation)


# Write a Python program that asks the user to enter three integer numbers.
# The program should output the largest of the three numbers.

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
if a > b and a > c:
    lar = a
elif b > a and b > c:
    lar = b
else:
    lar = c
print("The largest number is", lar)


# Triangles can be classified based on their angles.
# A right triangle has one angle of 90°
# A obtuse triangle has one angle of more than 90°
# A triangle is acute if all three angles are less than 90°
# Write a program that asks the user for the values of three angles in degrees. First check if the entered values are valid.
# The values are only valid if they are >0 and if their sum is 180°. If the entered values

angl1 = int(input("Angl1 pls"))
angl2 = int(input("Angl2 pls"))
angl3 = int(input("Angl3 pls"))
resangl = ""
if (angl1 > 0) and (angl2 > 0) and (angl3 > 0) and (angl1 + angl2 + angl3 == 180):
    if (angl1 == 90) or (angl2 == 90) or (angl3 == 90):
        resangl = "right"
    elif (angl1 > 90) or (angl2 > 90) or (angl3 > 90):
        resangl = "obtuse"
    elif (angl1 < 90) or (angl2 < 90) or (angl3 < 90):
        resangl = "acute"
    print("The triangle is a", resangl, "triangle")
else:
    print("The input is not valid")
