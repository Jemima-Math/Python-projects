a = int(input("Enter your age: "))
print("Your age is: ",a)
# Conditional operators
# > , < , >= ,<= , == ,!=

if(a > 18):
    print("You can drive")
else:
    print("You cannot drive")


applePrice = 210
budget = 200
if(applePrice <= budget):
    print("Alexa, add 1 kg apples to the cart")
else:
    print("Alexa, do not add apples to the cart")


num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is Zero")
elif(num == 999):
    print("Number is Special")
else:
    print("Number is positive")



# nested if-else

num = 18
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


# Exercise:

time = int(input("Enter the time(0-23): "))
if(4 <= time < 12):
    print("Good Morning")
elif(time == 12):
    print("Good Noon")
elif(12 < time <= 17):
    print("Good Afternoon")
elif(17 < time <= 20):
    print("Good evening")
else:
    print("Good Night")
# it doesnot contaain minute and second
# use function inside python 'strptime' 
# it takes raw text 14:30:00 and turns it mathematically that python understad
 
from datetime import datetime

time_str = "18:45:30"
# %H = hour, %M = minute, %S = second
parsed_time = datetime.strptime(time_str, "%H:%M:%S")

print(parsed_time.hour)    # Output: 18
print(parsed_time.minute)  # Output: 45




time_str = "02:30 PM"
parsed_time = datetime.strptime(time_str, "%I:%M %p") # %I = hour(01-12),%p = AM or PM

print(parsed_time.hour)  # Output: 14 (Python automatically converts PM to 24-hour time!)




date_str = "2026-07-22 09:15"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

print(parsed_date.year)  # Output: 2026

# do the exercise like this in the below

from datetime import datetime
time_input = input("Enter the time (HH:MM or HH:MM:SS): ")

parsed_time = datetime.strptime(time_input, "%H:%M:%S").time()

h = parsed_time.hour
m = parsed_time.minute
s = parsed_time.second

if 4 <= h < 12:
    print("Good Morning")
elif h == 12 and m == 0 and s == 0:
    print("Good Noon")
elif (h == 12 and (m > 0 or s > 0)) or (12 < h <= 17):
    print("Good Afternoon")
elif 17 < h <= 20:
    print("Good Evening")
else:
    print("Good Night")