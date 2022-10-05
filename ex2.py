''''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd number
react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check). If check divides evenly into num,
tell that to the user. If not, print a different appropriate message.
'''

num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num % 2 == 0:
    print("The first number is even")
else:
    print("The first number is odd")

if int(num) % 4 == 0:
    print("and the first number is a multiple of 4")

if (num % num2 == 0):
    print("First number is also divisible by the second number")
else:
    print("First number is not divisible by the second number")
