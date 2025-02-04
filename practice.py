# pi = 3.141592653589793238462643383279502884197
# print(f"{pi:.2f}")
# num = pi * 10
# print(f"{num:.2f}")
# num2 = pi * 10000
# print(f"{num2:,.2f}")

#Magic Date Problem

# month = int(input("Enter a month(numeric form)"))
# day = int(input("Enter a day(numeric form)"))
# year = int(input("Enter a year(last two digits"))

# print(f"{month}/{day}/{year}")

# if month * day == year:
#     print("The date is magic")
# else: 
#     print("The date is not magic")

#Day of the Week Problem
# number = int(input("enter a number: "))

# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Error.. Try Again")

# #Area of Rectangles

# sq1_length = int(input("Enter the first square's length: "))
# sq1_width = int(input("Enter the first square's width: "))

# sq2_length = int(input("Enter the second square's length: "))
# sq2_width = int(input("Enter the second square's width: "))

# sq1_area = sq1_length * sq1_width
# sq2_area = sq2_length * sq2_width

# if sq1_area > sq2_area:
#     print("The first square has a greater area")
# elif sq2_area > sq1_area:
#     print("The second square has a greater area")
# else:
#     print("The areas are the same")

# # Roman Numerals

# number = int(input("Enter a number: "))

# if number == 1:
#     print("I")
# elif number == 2:
#     print("II")
# elif number == 3:
#     print("III")
# elif number == 4:
#     print("IV")
# elif number == 5:
#     print("V")
# elif number == 6:
#     print("VI")
# elif number == 7:
#     print("VII")
# elif number == 8:
#     print("VIII")
# elif number == 9:
#     print("IX")
# elif number == 10:
#     print("X")
# else:
#     print("Error... Try Again(Number 1-10)")

#Age Classifier
# age = int(input("enter your age: "))

# if age <= 1:
#     print("infant")
# elif 1 < age < 13:
#     print("child")
# elif 13 <= age < 20:
#     print("teen")
# else:
#     print("adult")

#Mass and Weight

# mass = int(input("Enter objects mass: "))

# weight = mass * 9.8

# if weight > 500:
#     print("Too heavy")
# elif weight < 100:
#     print("Too Light")
# else:
#     print("Just Right")


# Color Mixer
# color1 = input("Pick a color: ")
# color2 = input("Pick another color: ")

# if (color1 == "blue" and color2 == "red") or (color1 == "red" and color2 == "blue"):
#     print(f"When you mix {color1} and {color2} you get purple")
# elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
#     print(f"When you mix {color1} and {color2} you get orange")
# elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
#     print(f"When you mix {color1} and {color2} you get green")
# elif color1 == color2:
#     print(f"You chose {color1} twice, choose two different primary colors")
# else:
#     print("Must enter Primary Colors, Try again.")

#Book Club Points

books = int(input("Enter number of books purchased this month: "))

if books == 0:
    print("Earned 0 points")
elif books == 2:
    print("Earned 5 points")
elif books == 4:
    print("Earned 15 points")
elif books == 6:
    print("Earned 30 points")
elif books == 8:
    print("Earned 60 points")
else:
    print("Couldn't register number.. Try again")