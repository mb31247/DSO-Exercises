"""""
name = input("Enter name: ")
age = int(input("Enter age: "))
age_year = str((2022-age) + 100)
print(name + " you will turn 100 in " + age_year)

num = input(" Choose a random number: ")
print((name + " you will turn 100 in " + age_year + '\n')*int(num))
"""""

"""""
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num % 2 == 0:
    print("The first number is even")
else:
    print("The first number is odd")

if int(num) % 4 == 0:
    print("and the first number is a multiple of 4")

if (num%num2 == 0):
    print("First number is also divisible by the second number")
else:
    print("First number is not divisible by the second number")
"""""

a = [1,1,2,3,5,8,13,21,34,55,89]
for n in a:
    if n < 5:
        print(n)

a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
for n in a:
    if n < 5:
        b.append(n)
print(b)
