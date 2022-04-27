# Write a program that asks the user for given name, surname and field of study for a student.
# Store this data in a tuple and print the tuple.

name = input("Please enter the given name of the student:")
surname = input("Please enter the surname of the student:")
field = input("Please enter the field of study of the student:")
student_tuple = (name, surname, field)
print(student_tuple)


# Use this dictionary to build a program that:
# Reads a sentence from the user.
# Replaces all the words in the sentence with the corresponding Emoji.

emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}
user_phrase = input("Please enter a sentence:")
words = user_phrase.split()
new_string = ''
for word in words:
    if word in emoji_dict:
        new_string = new_string  + " " + emoji_dict[word]
    else:
        new_string = new_string + " " + word
print(new_string)


# A Caesar cipher is a simple encryption technique.
# The encryption using a Ceasar cipher replaces a letter in the plain text
# with a letter that is a fixed number down in the alphabet.
# Your task for the assignment is to implement a Caesar cipher with a shift of 5.
# The program should ask the user for a plain text sentence and print the encrypted text.


user_phrase = input("Please enter a sentence: ")
user_phrase = user_phrase.lower()
new_phrase = ''
reg_alp = ["a", "b", "c", "d", "e", "f", "g", "h",
           "i", "j", "k", "l", "m", "n", "o", "p",
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
shifted_alp = ["f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]
for letter in user_phrase:
    if letter in reg_alp:
        new_phrase += shifted_alp[reg_alp.index(letter)]
    else:
        new_phrase += letter
print("The encrypted sentence is:", new_phrase)


# Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift.
# The program should ask the user for a number of characters for the shift first.
# Next the program should ask the user for a plain text sentence and print the encrypted text.

shift_num = input("Please enter the number of places to shift: ")
user_phrase = input("Please enter a sentence: ")
user_phrase = user_phrase.lower()
new_phrase = ''
reg_alp = "abcdefghijklmnopqrstuvwxyz"
shifted_alp = reg_alp*2
if shift_num.isdecimal() and int(shift_num) < 26:
    for letter in user_phrase:
        if letter in reg_alp:
            new_phrase += shifted_alp[reg_alp.find(letter) + int(shift_num)]
        else:
            new_phrase += letter
else:
    print("You need to enter a number between 0 and 25!")
print("The encrypted sentence is:", new_phrase)
