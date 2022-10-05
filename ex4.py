'''''
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

list = []
userInput = int(input("Enter a number: "))
for div_number in range(1, userInput + 1):
    if userInput % div_number == 0:
        list.append(div_number)
print(list)
