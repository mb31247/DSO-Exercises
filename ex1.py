"""""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:
Add on to the previous program by asking the user for
another number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

name = input("Enter name: ")
age = int(input("Enter age: "))
age_year = str((2022-age) + 100)
print(name + " you will turn 100 in " + age_year)

num = input(" Choose a random number: ")
print((name + " you will turn 100 in " + age_year + '\n')*int(num))

