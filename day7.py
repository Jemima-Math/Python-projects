# functions: 1. Built-in function
#            2. User-defined function

# a = 9
# b = 8 
# gmean1 = (a * b)/(a + b)
# print(gmean1)
#
# if(a > b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")

# we will use functions for calculating this for more.

def isGreater(a, b):
    if(a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass # we use this when we write a function but want to use later,without pass it will show error.

def calculateGmean(a , b):
    mean = (a * b)/(a + b)
    print(mean)

a = 9
b = 8
isGreater(a ,b)
calculateGmean(a, b)

c = 8
d = 7
isGreater(c, d)
calculateGmean(c, d)

def average(a, b):
    print("The average is ",(a + b)/2)

average(4, 6)

# defaul case:
# 1:
def average(a=9, b=1):
    print("The average is ",(a + b)/2)

average(1, 5) # it will ignore previous value of a and b and give answer

# 2:
def average(a=9, b=1):
    print("The average is ",(a + b)/2)

average(5) #for this it will take a=5,b=1

# 3:
def average(a=9, b=1):
    print("The average is ",(a + b)/2)

average(b=9)

def average(*numbers): # using * before numbers because in between () there will be more number than 2,called tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ",sum / len(numbers))
average(5 ,6 ,2 , 7)

def average(*numbers): 
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers) # using return will store the value,so we can use it further calculation.but in previous code we cant do double as it is not stored,will show error
c = average(5 ,6 ,2 , 7)
print("Average is: ",c)
double_avg = c * 2
print("The double of the average: ", double_avg)
