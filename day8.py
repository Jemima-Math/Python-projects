# list:

marks = [3, 5, 6, "Jemima", True, 6556, "Mango", "Moon"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-3]) # len(marks - 3)

if 7 in marks:
    print("Yes")
else:
    print("No")

if "6" in marks:
    print("Yes")
else:
    print("No")

if "Jemima" in marks:
    print("Yes")
else:
    print("No")

if "mima" in "Jemima":
    print("Yes")
else:
    print("No")

print(marks[1:-1])
print(marks[1:8:2])
print(marks[1:8:3])
print(marks[:]) # python will take 0 : len(marks)
print(marks[:7]) # python will take 0:7
print(marks[2:]) # python will take 2:len(marks)

# list comprehension:

lst= [i*i for i in range(10)]
print(lst)
lst= [i*i for i in range(10) if i%2 == 0]
print(lst)