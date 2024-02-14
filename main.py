import math
import time

# print("I Love Pizza");
# print("It is really good");

# VARIABLES ✘
# STRING 
# name = "Faizan"
# print("Hello " + name)
# print(type(name)) # check data type

# first_name = "Faizan"
# last_name = "Shaikh"
# print(first_name + " " + last_name)

# NUMBER - INT
# age = 23
# age += 1
# print(age)
# print("my age is " + str(age))
# print(type(age))

# FLOAT
# height = 250.5
# print(height)
# print(type(height))
# print("Your height is " + str(height))

# BOOLEAN
# human = True
# print(human)
# print(type(human))
# print("Are you a human " + str(human))

# MULTIPLE ASSIGNMENT  🔠
# name = "Faizan"
# age = 23
# attractive = True
# name, age, attractive = "Faizan", 23, True
# print(name)
# print(age)
# print(attractive)

# Faizan  = 30
# Shaikh = 30
# Poojan   = 30
# Faizan  = Shaikh = Poojan = 30
# print(Faizan)
# print(Shaikh)
# print(Poojan)

# STRING METHODS 〰️
# name = "Faizan Shaikh"
# print(len(name))
# print(name.find("F"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit()) # True / False
# print(name.isalpha()) # True / False
# print(name.count("N"))
# print(name.replace("z", "x"))
# print(name * 3)

#  TYPE CAST 💱
# x = 1
# y = 2.0
# z = "3"
# y = int(y)
# print(str(x))
# print(y)
# print(float(z))
# print(float(z) * 3)

# USER INPUT ⌨️
# name = input("What is your name?")
# age = int(input("What is your age?"))
# height = float(input("What is your height?"))
# print("Hello, " + name)
# print("Age, " + str(age))
# print("Height, " + str(height))

# MATH FUNCATIONS 🧮
# pi = 3.14
# x,y,z = 1,2,3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi)) # -3.14 > 3.14
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(z,y,x))

# STRING SLICING ✂️
# name = "Faizan Shaikh"
# first_name = name[0:6]
# last_name = name[len(first_name) + 1:len(name)]
# funcky_name = name[::2] # [start:stop:step]
# reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funcky_name)
# print(reversed_name)

# web1 = "http://google.com"
# web2 = "http://faizan.com"
# slice = slice(7, -4)
# print(web1[slice])
# print(web2[slice])

# IF STATEMENTS 🤔
# age = int(input("How old are you? "))
# if age == 100:
#     print("You\'re an old!")
# elif age >= 18:
#     print("You\'re an adult!")
# elif age < 0:
#     print("You\'re not been born yet!")
# else :  
#     print('You\'re a minor!')

# Logical Operator 🔣 [and, or, not]
# temp = int(input("What is the temperature outside? "))

# if temp >= 0 and temp <= 30:
#     print("It's cold out there.")
# elif not(temp > 0 or temp > 30):
#     print("It's freezing out there.")

# WHILE LOOP 🔄
# name = ""
# name = None
# while not name :
#     name = input("Enter your name: ")
# print(name)

# FOR LOOPS ➰

# for i in range(10):
#     print(i + 1)
# for i in range(50, 100,2):
#     print(i)
# for i in "Faizan Shaikh":
#     print(i)
# for seconds in range(10, 0, -1): 
#     print(seconds)
#     time.sleep(1)
# print(f"Time's up!")

# NESTED LOOP
# rows = int(input("How many rows? "))
# columns = int(input("How many columns? "))
# symbol = input("Enter a symbol to use? ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# LOOP CONTROL STATEMENTS = Change a loops execution from its normal sequnce.
# break = used to terminate the loop entirely.
# continue = skips to the next iteration of the loop.
# pass = does noting, acts as a placeholder

# while True:
#     name = input("Enter your name:")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

# LIST = used to store multiple items in a single variable
# names = ["Faizan", "Poojan", "Nikunj", "Gotu"]
# names.append("Shaikh")
# names.remove("Poojan")
# names.pop()
# names.insert(2, "Shaikh")
# names.sort()
# names.clear()
# print(names)

# 2D LIST  =  a list of lists
# names1 = ["Faizan", "Poojan", "Nikunj", "Gotu"]
# names2 = ["Faizan", "Poojan", "Nikunj", "Gotu"]
# names3 = ["Faizan", "Poojan", "Nikunj", "Gotu"]
# names = [names1, names2, names3]
# print(names)

# TUPLES = Collection which is ordered and unchangeble used to group together related data
# student = ("Faizan", 23, "male")
# print(student.count("Faizan"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Faizan" in student:
#     print("Faizan is here!")

# SET = collection which is unordered, unindexed. No duplicate values
names1 = {"Faizan", "Poojan", "Nikunj"}
names2 = {"Faizan", "Anas", "Gotu"}
names = names1.union(names2)
# names1.add("Gotu")
# names1.remove("Faizan")
# names1.clear()
# names1.update(names2)
# print(names1)
# print(names2.difference(names1))
# print(names2.intersection(names1))
for  name in names:
    print(name)