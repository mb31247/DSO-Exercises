from datetime import datetime
t = datetime.now()
year = t.year
#print(year)

name = raw_input("Enter your name")
age = int(input("Enter your age"))
#print ('Trial')
print'Your name is ' + name +  ' and your age is', age
print'\nYou will turn 100 years in', year+(100-age)
string = 'You will turn 100 years in '+str(year+(100-age))+'\n'
times = int(input("How many times do you want to see the previous message?---> "))
print times * string
#print(age)
