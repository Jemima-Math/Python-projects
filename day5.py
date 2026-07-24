# practice:

# 1.change temparature from celsius to fahrenheit:

tempC = float(input("Enter the value(in celsius): "))
tempF = (tempC * 1.8) + 32
print(tempF)

# 2.Write a simple condition checker that tests password length and specific characters:

password = "Jemima2026"
if (len(password) >= 8 and password.isalnum()):
    print("strong password")
else:
    print("Weak password")

# 3.write a script that takes a sentence and turn it into a clean title

text = "   python is AWESOME!   "
print(text.strip("   ").title())

# 4.Write a script that validates if a chosen username is good for registration.

username = "YouAndMe"
if 3 < len(username) < 15 and username.isalnum():
    print("Username Valid")
else:
    print("username not valid")

# 5.Check a number is even or odd:

n = int(input("Enter a number: "))
if (n % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")

# 6.check n:

n = int(input("Enter the value of n: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0 and n % 5 != 0:
    print("Fizz")
elif n % 5 == 0 and n % 3 != 0:
    print("Buzz")
else:
    print(n)

# 7.List inspecter:

cart = ["apple","Banana","Mango","Bread","Egg"]
item = input("Enter the item: ")
if item in cart:
    print("Present in the stock")
else:
    print("out of stock!Adding item to the cart.")
    cart.append(item)
    print("Updated cart: ",cart)
# use .append() to add a single item to the very end of a list)

# 8.Leap Year find:

n = int(input("Enter the year: "))
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print(n,"is a Leap Year")
else:
    print(n,"is not a Leap year")

# 9.palindrome

str = "Nurses Run"
strNew = str.lower().replace(" ","") # using replace instead of strip because strip only cut first and last gaps
strRev = strNew[::-1] # use [::-1] to reverse a string
if strNew == strRev:
    print("It is a palindrome")
else:
    print("Not apalindrome")

# 10.Calculatevthe final bills for a online store based on total price and membership status:

total_amount = float(input("Enter total value: "))
is_vip = input("Are you a VIP member(Yes/No): ")
if is_vip == "Yes" and total_amount > 2000:
    finalBill = total_amount * 0.80
    print("Apply a 20 % discount and free shipping!Final Bill = ",finalBill)
elif is_vip == "Yes" and total_amount <= 2000:
    finalBill = total_amount * 0.90
    print("Apply a 10 % discount and free shipping!Final Bill = ",finalBill)
elif is_vip == "No" and total_amount > 2000:
    finalBill = (total_amount * 0.95) + 50
    print("Apply a 5% discount and $50 shipping fee!Final Bill = ",finalBill)
else:
    finalBill = total_amount + 50
    print("0% discount and $50 shipping fee!Final Bill = ",finalBill)

# if i want to round off the answer,use round()
# like for finalBill to round off to 2 decimal places,
# "......!Final Bill",round(finalBill,2)