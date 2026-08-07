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

l = [31, 45, 5, 3, 9]
l.append(7) # append will add 
print(l)
# print(l.append(7).sort())

l = [31, 45, 5, 3, 9]
l.sort()  # sort in assending order 
print(l)

l = [31, 45, 5, 3, 9]
l.sort(reverse=True)  # sort in desending order 
print(l)

l = [31, 45, 5, 3, 9]
l.reverse()  # just reverse the list
print(l)

l = [31, 45, 5, 1, 3, 9]
print(l.index(1))  # posion of 1

l = [31, 1, 45, 5, 1, 3, 9]
print(l.count(1))  # how many 1 has

l = [31, 45, 5, 1, 3, 9]
m = l.copy()
print(l)

l = [31, 45, 5, 38, 1, 3, 9]
l.insert(1 , 899)  # 1 is denoted the position 899 will take in list
print(l)

l = [31, 45, 5, 1, 3, 9]
m =[900, 1000, 1111]
l.extend(m)  # if we want to extend l,m will add in last
print(l)
# another way to extend:

l = [31, 45, 5, 1, 3, 9]
m =[900, 1000, 1111]
k = l + m
print(k)