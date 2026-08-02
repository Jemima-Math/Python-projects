# Match case:
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")


# for loop:

name = 'Abhishek'
for i in name:
    print(i)
    if(i == "b"):
        print("This is something special")

# colors = ["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(5):
#     print(k + 1)

# for k in range(1, 20001): # it will print 1-20000
#     print(k)

# for k in range(1, 12, 3): # it will add the last point to first one and continue
#     print(k)


# while loop:

i = int(input("Enter the number: "))
while(i <= 3):
    print(i) # it will not print the last given number 

i = int(input("Enter the number: "))
while(i <= 3):
    i = int(input("Enter the number: "))
    print(i)
 
count = 5
while (count > 0):
    print(count)
    count = count - 1 # using + will create a infinity loop
else:
    print("I am inside else")

# do-while

# do {
#     # loop body;
# }while(condition)

# in do while one iteration must run.


# break

for i in range(12):
    if(i == 10):
        break
    print("5 X", i+1 ,"=" , 5 *(i+1)) # using i will omit out the 5 * 10 =50 line

# continue

for i in range(12):
    if(i == 10):
        print("Skip this iteration")
        continue
    print("5 X", i ,"=" , 5 *(i))