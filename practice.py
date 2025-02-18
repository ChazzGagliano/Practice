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

# books = int(input("Enter number of books purchased this month: "))

# if books == 0:
#     print("Earned 0 points")
# elif books == 2:
#     print("Earned 5 points")
# elif books == 4:
#     print("Earned 15 points")
# elif books == 6:
#     print("Earned 30 points")
# elif books == 8:
#     print("Earned 60 points")
# else:
#     print("Couldn't register number.. Try again")

#Software Sales
# number_of_packages = int(input("Enter number of packages purchased: "))

# if 10 <= number_of_packages <= 19:
#     print("10% Discount")
# elif 20 <= number_of_packages <= 49:
#     print("20% Discount")
# elif 50 <= number_of_packages <= 99:
#     print("30% Discount")
# elif number_of_packages >= 100:
#     print("40% Discount") 
# else: 
#     print("No Discount")

# Roulette Wheel Colors
# number = int(input("Enter a pocker number 0 through 36: "))

# if 0 <= number <= 36:
#     if number == 0:
#         print("green")
#     elif 1 <= number <= 10:
#         if number % 2 == 0:
#             print("black")
#         else: 
#             print("red")
#     elif 11 <= number <= 18:
#         if number % 2 == 0:
#             print("red")
#         else: 
#             print("black")
#     elif 19 <= number <= 28:
#         if number % 2 == 0:
#             print("black")
#         else: 
#             print("red")
#     elif 29 <= number <= 36:
#         if number % 2 == 0:
#             print("red")
#         else:
#             print("black")
# else:
#     print("Need a number 0 through 36")

#Money Counting Game
# number_of_pennies = int(input("Enter number of pennies: "))
# number_of_nickels = int(input("Enter number of nickels: "))
# number_of_dimes = int(input("Enter number of dimes: "))
# number_of_quarters = int(input("Enter number of quarters: "))

# pennies = .01 * number_of_pennies
# nickels = .05 * number_of_nickels
# dimes = .10 * number_of_dimes
# quarters = .25 * number_of_quarters

# total = pennies + nickels + dimes + quarters

# if total == 1.0:
#     print("You won the game")
# elif total > 1.0:
#     print(f"More than a dollar by ${total - 1.0:.2f}")
# else:
#     print(f"Less than a dollar by ${1.0 - total:.2f}")

#Color mixer
# color1 = input("Enter the first color: ")
# color2 = input("Enter the second color: ")

# if color1 == "red":
#     if color2 == "green":
#         print("The two colors are complementary")
#     elif color2 == "orange" or color2 == "yellow" or color2 == "blue" or color2 == "purple":
#         print("The two colors are not complementary")
#     else:
#          print('You did not enter one of red, orange, yellow, green, blue or purple')
# elif color1 == "green":
#     if color2 == "red":
#         print("The two colors are complementary")
#     elif color2 == "orange" or color2 == "yellow" or color2 == "blue" or color2 == "purple":
#         print("The two colors are not complementary")
#     else:
#          print('You did not enter one of red, orange, yellow, green, blue or purple')
# elif color1 == "yellow":
#     if color2 == "purple":
#         print("The two colors are complementary")
#     elif color2 == "orange" or color2 == "green" or color2 == "red" or color2 == "blue":
#         print("The two colors are not complementary")
#     else:
#          print("You did not enter one of red, orange, yellow, green, blue, or purple")
# elif color1 == "purple":
#     if color2 == "yellow":
#         print("The two colors are complementary")
#     elif color2 == "orange" or color2 == "yellow" or color2 == "red" or color2 == "blue":
#         print("The two colors are not complementary")
#     else:
#          print('You did not enter one of red, orange, yellow, green, blue or purple')
# elif color1 == "blue":
#     if color2 == "orange":
#         print("The two colors are complementary")
#     elif color2 == "purple" or color2 == "green" or color2 == "yellow" or color2 == "red":
#         print("The two colors are not complementary")
#     else:
#          print('You did not enter one of red, orange, yellow, green, blue or purple')
# elif color1 == "orange":
#     if color2 == "blue":
#         print("The two colors are complementary")
#     elif color2 == "yellow" or color2 == "red" or color2 == "green" or color2 == "purple":
#         print("The two colors are not complementary")
#     else:
#         print('You did not enter one of red, orange, yellow, green, blue or purple')
# else: 
#     print('You did not enter one of red, orange, yellow, green, blue or purple')

#Leap Year

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

#Restaurant Selector
# question1 = input("Is anyone in your party a vegetarian? (yes/no) ")
# question2 = input("Is anyone in your party a vegan? (yes/no) ")
# question3 = input("Is anyone in your party gluten-free? (yes/no) ")

# if question2 == "yes":
#     print("Corner Cafe")
#     print("Chef’s Kitchen")
# elif question1 == "yes":
#     if question3 == "yes":
#         print("Main Street Pizza Company")
#         print("Corner Cafe")
#         print("Chef’s Kitchen")
#     else:
#         print("Main Street Pizza Company")
#         print("Mama's Fine Italian - Vegetarian")
#         print("Corner Cafe")
#         print("Chef’s Kitchen")
# else:
#     if question3 == "yes":
#         print("Main Street Pizza Company")
#         print("Corner Cafe")
#         print("Chef’s Kitchen")
#     else:
#         print("Joe’s Gourmet Burgers")
#         print("Main Street Pizza Company")
#         print("Mama's Fine Italian - Vegetarian")
#         print("Corner Cafe")
#         print("Chef’s Kitchen")

#Shipping Charges

# weight = int(input("Enter weight of package(in pounds) for shipping price: "))

# if weight <= 2:
#     print("$1.50")
# elif 2 < weight <= 6:
#     print("$3.00")
# elif 6 < weight <= 10:
#     print("$4.00")
# else:
#     print("$4.75")

#CHAPTER 4

#Distance Traveled
# mph = int(input("What is the speed of the vehicle in mph? "))
# hour = int(input("How many hours has it traveled? "))

# count = 1
# distance_traveled = 0
# print("Hour Distance Traveled")
# while count <= hour:
#     distance_traveled += mph
#     print(f"{count}           {distance_traveled}")
#     count += 1

#Population
# starting_number = int(input("Enter number of starting organisms: "))
# population_increase = float(input("Enter daily average population increase(as percentage): "))
# number_of_days = int(input("Enter number of days left to multiply: "))
    
# day_count = 1
# population_increase = 1 + (population_increase / 100)
# print("Day Approximate Population")
# while day_count <= number_of_days:
#     print(f"{day_count}   {starting_number:.4f}")
#     starting_number *= population_increase
#     day_count += 1


# n = int(input("Enter number: "))
# count = 1 

# while count <= n:
#     if count % 7 == 0:
#         print(f'{n} is a multiple of 7')
#     count += 1

# n = int(input("Enter number: "))  
# count = 1  

# while count <= n:  
#     if count % 7 == 0:  # Check if 'count' (not 'n') is a multiple of 7
#         print(f'{count} is a multiple of 7')  
#     count += 1  # Always increment count to avoid an infinite loop

# while True:
#     temp = int(input("Enter the temperature:"))
#     if 78 <= temp >= 100:
#         print("Temperature accepted.")
#         break
# print("Enter the temperature again.")

# count = 1
# while True:
#     number = int(input("Enter a number 1 through 100"))
#     if 1 <= number <= 100:
#         while count <= 10:
#             print(f"{number * count}")
#             count += 1
#     break
    


# while True:
#     number = int(input("Enter a number 1 through 100"))
#     if 1 <= number <= 100:
#         for i in range(0, 11):
#             print(f"{number} x {i} = {number * i}")
#     break

# number = int(input("Enter a number: "))

# for i in range(1, number + 1):
#     for i2 in range(1, i + 1):
#         print(f" {i2} ")
#     print()

# Distance Traveled
# speed = int(input("What is the speed of the vehicle in mph: "))
# hour = int(input("how many hours has it traveled: "))
# print("Hour Distance Traveled")
# for i in range(1, hour + 1):
#     distance = speed * i
#     print(f"{i}      {distance}")

# Population
# start = int(input("Starting number of organisms: "))
# daily_increase = float(input("Daily increase in percentage: "))
# days = int(input("Number of days: "))

# print("Day   Approximate Population")
# calcuation = 1 + (daily_increase / 100)
# for i in range(1, days + 1):
#     print(f"{i}  {start:.2f}")
#     start *= calcuation

#Bug Collector
# days = 5
# total_bugs = 0

# for i in range(1, days + 1):
#     number = int(input(f"How many bugs did you collect on day {i}?: "))
#     total_bugs += number
# print(f"You collected {total_bugs} bugs in total.")

#Calories Burned
# calories = 4.2
# total = 0

# for i in range(1, 31):
#     total += calories 
#     if i % 5 == 0:
#         print(f"{i}: {total:.0f} calories burned.")


#Budget Analysis
# budget = int(input("Enter your budget for the month (Enter 0 to exit): "))
# total_expenses = 0

# while True: 
#     expense = int(input("Enter your expense: "))
#     total_expenses += expense
#     if expense == 0:
#         break
# if total_expenses > budget:
#     print(f"You're over budget by ${total_expenses - budget}")
# elif budget > total_expenses:
#     print(f"You stayed under budget by ${budget - total_expenses}")
# else:
#     print("You broke even")

#Distance Traveled
# speed = int(input("What is the speed of the vehicle in mph: "))
# hour = int(input("How many hours did you travel: "))

# distance_traveled = 0
# print("Hour   Distance_Traveled")
# for i in range(1, hour + 1):
#     distance_traveled = speed * i
#     print(f"{i}    {distance_traveled}")

#Average Rainfall
# years = int(input("How many years: "))
# whole_total = 0
# total_months = 0
# for i in range(1, years + 1):
#     total = 0
#     for i2 in range(1, 13):
#         rain = int(input(f"How much rain in month {i2} of year {i} in inches: "))
#         whole_total += rain
#         total_months += 1
#         total += rain 
#     average = total / 12
#     print(f"{total} inches total rain in year {i}")
#     print(f"{average} is the average in year {i}")
# print(f"{total_months} months entire period")
# print(f"{whole_total} inches entire period")
# print(f"{whole_total / total_months} is the average inches in the entire period")

#Celsius to Farenheit
# for i in range(0, 21):
#     f = (i * 1.8) + 32
#     print(f"C{i} = F{f:.0f} degrees")

# count = 0
# while True:
#     number = (input("Enter number: "))
#     number = str(number)
#     count += 1
#     if number == "stop":
#         print(count)
#         break

# right_value = 70
# attempts = 0

# while True:
#     number = int(input("Enter a number: "))
#     attempts += 1
    
#     if number == right_value:
#         print(f"Correct! It took you {attempts} guesses.")
#         break
#     elif number < right_value:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is too high.")

# Paint Job Estimator

# def main():
#     square_feet = int(input("Enter the square feet of walls: " ))
#     paint_price = float(input("Enter the price paint per gallon: "))
#     paint_job_estimator(square_feet, paint_price)

# def paint_job_estimator(square_feet, paint_price):
#     per_square = 112
#     hours = 8
#     labor = 35
#     quantity = (square_feet + 111) // per_square
#     number_gallons_paint_required = 1
#     number_gallons_paint_required *= quantity
#     hours_labor = quantity * hours
#     total_paint_price = paint_price * number_gallons_paint_required
#     price_labor = hours_labor * labor
#     total = price_labor + total_paint_price
#     print(f"The number of gallons of paint required: {number_gallons_paint_required}")
#     print(f"The hours of labor required: {hours_labor}")
#     print(f"The cost of paint: ${total_paint_price:.2f}")
#     print(f"The labor charges: ${price_labor:.2f}")
#     print(f"The total cost of paint job: ${total:.2f}")

# main()

# Maximum of Two Values
# def max(number1, number2):
    
#     if number1 > number2:
#         print(number1)
#     elif number2 > number1:
#         print(number2)
#     else:
#         print("Both numbers are equal")

# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter a different number: "))

# max(number1, number2)

# import math

# def apothem(side_length, number_of_sides):
#     return side_length / (2 * math.tan(math.radians(180 / number_of_sides)))

# def area(side_length, number_of_sides):
#     perimeter = number_of_sides * side_length
#     apothem_value = apothem(side_length, number_of_sides)
#     return 0.5 * perimeter * apothem_value

# number_of_sides = int(input("Enter the number of sides: "))
# side_length = float(input("Enter the side length: "))

# polygon_area = area(side_length, number_of_sides)

# print(f"{polygon_area:.2f}")

#Kilometer Converter
# converter = 0.6214
# def main():
#     kilometers = float(input("Enter a distance in kilometers: "))
#     kilometer_converter(kilometers)

# def kilometer_converter(km):
#     miles = km * converter
#     print(f"{km} kilometers is equivalent to {miles:.2f} miles")
# main()

#Sales Tax Refactoring
# county_tax = .03
# state_tax = .05

# def main():
#     purchase = float(input("Enter the price of your purchase: "))
#     tax_program(purchase)

# def tax_program(purchase):
#     county_sales_tax = purchase * county_tax
#     print(f"The county sales tax is {county_sales_tax:.2f}")
#     state_sales_tax = purchase * state_tax
#     print(f"The state sales tax is {state_sales_tax:.2f}")
#     total = purchase + state_sales_tax + county_sales_tax
#     print(f"The total of the purchase is ${total:.2f}")
# main()

#How Much Insurance
# def main():
#     price = float(input("Enter replacement cost: "))
#     minimum_cost(price)

# def minimum_cost(price):
#     minimum = .80
#     total = price * minimum
#     print(f"The minium amount for the insurance for the property should be ${total:.2f}")

# main()

#Automobile Costs

def main():
    loan = float(input("Enter your monthly loan payment: "))
    insurance = float(input("Enter your monthly insurance payment: "))
    gas = float(input("Enter your monthly gas payment: "))
    oil = float(input("Enter your monthly oil payment: "))
    tires = float(input("Enter your monthly tires payment: "))
    maintenance = float(input("Enter your monthly maintenance payment: "))
    total_expenses(loan, insurance, gas, oil, tires, maintenance)

def total_expenses(loan, insurance, gas, oil, tires, maintenance):
    annual = 12
    monthly_total = loan + insurance + gas + oil + tires + maintenance
    annual_total = monthly_total * annual
    print(f"The monthly total is ${monthly_total:.2f} and the annual total is ${annual_total:.2f}.")
    
main()

