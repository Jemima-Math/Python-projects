a = ("Enter the name: ")
print("My name is",a)

x = input("Enter the number: ")
y = input("Enter the number: ")

# use typecasting or it will show error
a = int(x) + int(y)
b = int(x) - int(y)
c = int(x) * int(y)
d = int(x) / int(y)

print(a,b,c,d)

name = "Jemima"
friend = "Nishat"
print("hello,", name)

# string start from [0]
print(friend[0])
print(friend[1])
print(friend[2])
print(friend[3])
print(friend[4])
print(friend[5])
# print(friend[6]) it throws an error

apple = '''He said,
"hi Jemima
how are you?
Let,s go somewhere to eat'''

# use ''' or """ to find string names where there is line change or double coting between single coting
# use 'for' loop for determine the string of big statement or paragraph

for character in apple:
    print(character)

# String Slicing 
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:5])
print(fruit[0:-3]) # it means print(fruit[0:len(fruit)-3])
print(fruit[-3:-1])

#exercise:
nm = "Banana"
print(nm[-4:-2])