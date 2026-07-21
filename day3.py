# strings are immutable
a = "!!! Jadavpur !!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # edit out only the last part of string

a = "!!! Jadavpur !!!!!!!! Jadavpur"
print(a.replace("Jadavpur", "University"))
print(a.split(" "))
print(a.count("Jadavpur"))

studyTopic = "learning ab0ut pythoN"
print(studyTopic.capitalize()) # along with capitalization,it will correct errors in between 

str1 = "Welcome to Jadavpur!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10)) #first find the string of 4 to 10 ,then check

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # it will read the first 'is',ignore 's
print(str1.find("ishh")) # find show -1 if not contain in string
# print(str1.index("ishh")) using index show error

# Alphanumeric - isalnum()
# this method returns true only if the entire string only contains A-Z,a-z,0-9

str1 = "WelcometoJadavpur"
print(str1.isalnum()) #true

str1 = "hello world"
print(str1.islower())  #true

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable) # as \n is used ,it is not printable, answer is false

str1 = "       "  #using Spacebar
print(str1.isspace())

str1 = "World Health Organisation" # returns true if the first letter of every word is capitalize
print(str1.istitle()) #true

str2 = "To kill a Mocking Bird"
print(str2.istitle()) #false

str1 = "Python is Interpreted Language"
print(str1.startswith("Python"))

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())