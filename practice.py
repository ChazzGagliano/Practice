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

#Area of Rectangles

sq1_length = int(input("Enter the first square's length: "))
sq1_width = int(input("Enter the first square's width: "))

sq2_length = int(input("Enter the second square's length: "))
sq2_width = int(input("Enter the second square's width: "))

sq1_area = sq1_length * sq1_width
sq2_area = sq2_length * sq2_width

if sq1_area > sq2_area:
    print("The first square has a greater area")
elif sq2_area > sq1_area:
    print("The second square has a greater area")
else:
    print("The areas are the same")