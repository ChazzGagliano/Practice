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
# import math

# def main():
#     square_feet = int(input("Enter the square feet of wall space: " ))
#     paint_price = float(input("Enter the price paint per gallon: "))
#     paint_job_estimator(square_feet, paint_price)

# def paint_job_estimator(square_feet, paint_price):
#     per_square = 112
#     hours = 8
#     labor = 35
#     quantity = math.ceil(square_feet / per_square)
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

# def main():
#     number1 = int(input("Enter a number: "))
#     number2 = int(input("Enter a different number: "))
#     max(number1, number2)

# def max(number1, number2):
    
#     if number1 > number2:
#         print(F"{number1} is greater")
#     elif number2 > number1:
#         print(f"{number2} is greater")
#     else:
#         print("Both numbers are equal")
# main()

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

# def main():
#     loan = float(input("Enter your monthly loan payment: "))
#     insurance = float(input("Enter your monthly insurance payment: "))
#     gas = float(input("Enter your monthly gas payment: "))
#     oil = float(input("Enter your monthly oil payment: "))
#     tires = float(input("Enter your monthly tires payment: "))
#     maintenance = float(input("Enter your monthly maintenance payment: "))
#     total_expenses(loan, insurance, gas, oil, tires, maintenance)

# def total_expenses(loan, insurance, gas, oil, tires, maintenance):
#     annual = 12
#     monthly_total = loan + insurance + gas + oil + tires + maintenance
#     annual_total = monthly_total * annual
#     print(f"The monthly total is ${monthly_total:.2f} and the annual total is ${annual_total:.2f}.")

# main()

#Math Quiz
# import random

# def main():
#     x = random.randint(1, 1000)
#     y = random.randint(1, 1000)
#     math_problem(x, y)

# def math_problem(x, y):
#     print(f"  {x}")
#     print(f"+ {y}")
#     number = int(input("Enter the sum of the two numbers: "))
#     if number == x + y:
#         print("Correct!")
#     else:
#         print("Incorrect!")

# main()

#Property Tax
# def main(): 
#     value = float(input("Enter value of property: "))
#     property_tax(value)

# def property_tax(value):
#     assessment_value = value * .60
#     assessment_unit = 100
#     tax_rate = .72
#     property_tax_due = (assessment_value / assessment_unit) * tax_rate
#     print(f'The tax for the acre assessed at ${assessment_value:.2f} will be ${property_tax_due:.2f}')

# main()

#Stadium_Seating

# def main():
#     quantity_a = int(input("How many seats were sold in Class A: "))
#     quantity_b = int(input("How many seats were sold in Class B: "))
#     quantity_c = int(input("How many seats were sold in Class C: "))
#     stadium_income(quantity_a, quantity_b, quantity_c)

# def stadium_income(quantity_a, quantity_b, quantity_c):
#     price_a = 20
#     price_b = 15
#     price_c = 10

#     total_income = (quantity_a * price_a) + (quantity_b * price_b) + (quantity_c * price_c)
#     print(f"Total income for stadium ticket sales: ${total_income:.2f}")

# main()

#Monthly Sales Tax
# def main():
#     month_sales = float(input("Enter total sales for the month: "))
#     monthly_sales_tax(month_sales)

# def monthly_sales_tax(month_sales):
#     county_sales_tax = .05
#     state_sales_tax = .025
#     total_sales_tax = (month_sales * county_sales_tax) + (month_sales * state_sales_tax)
#     print(f"Amount of county sales tax: ${month_sales * county_sales_tax}")
#     print(f"Amount of state sales tax: ${month_sales * state_sales_tax}")
#     print(f"Total sales tax: ${total_sales_tax}")

# main()

# count = 1
# while count <= 5:
#     addition = count + count
#     sub = count - count
#     product = count * count
#     quotient = count / count
#     if count % 2 != 0:
#         print(f"{count} + {count} = {addition}")
#         print(f"{count} - {count} = {sub}")
#         print(f"{count} x {count} = {product}")
#         print(f"{count} / {count} = {quotient}")
#     count += 1

#Feet to Inches
# def main():
#     feet = int(input("Enter how many feet: " ))
#     feet_to_inches(feet)

# def feet_to_inches(feet):
#     inch_converter = 12
#     inches = feet * inch_converter
#     print(f"{feet} ft is equivalent to {inches} inches.")

# main()

#Falling Distance
# def falling_distance(t):
#     g = 9.8

#     for t in range(1, 11):
#         d = .5 * g * (t ** 2)
#         print(f"{t} seconds = {d:.2f} meters")
#         t += 1

# falling_distance(10)
# def main():
#     mass = float(input("Enter the mass in kilograms: "))
#     velocity = int(input("Enter the speed in meters per second: "))
#     kinetic_energy(mass, velocity)
    
# def kinetic_energy(mass, velocity):
#     conversion = 0.5 * mass * (velocity ** 2)
#     print(f"The objects kinetic engergy is: {conversion:.2f}")

# main()

#Odd/Even Numbers
# import random

# def main():
#     even = 0
#     odd = 0
#     for i in range(1, 101):
#         number = random.randint(1, 1000)
#         if number % 2 != 0:
#             odd += 1
#         else:
#             even += 1
#     print(f"{odd} odd numbers and {even} even numbers.")

# main()

#Test Average and Grade
# import math

# def main(): 
#     test1 = int(input("Enter grade for first test: "))
#     test2 = int(input("Enter grade for second test: "))
#     test3 = int(input("Enter grade for third test: "))
#     test4 = int(input("Enter grade for fourth test: "))
#     test5 = int(input("Enter grade for fifth test: "))
#     determine_grade(test1, test2, test3, test4, test5)
#     result = calc_average(test1, test2, test3, test4, test5)       
#     print(f"The class average is {result}")

# def calc_average(test1, test2, test3, test4, test5):
#     sum = test1 + test2 + test3 + test4 + test5 
#     average = math.ceil(sum / 5)
#     return average

# def determine_grade(test1, test2, test3, test4, test5):
#     for i in test1, test2, test3, test4, test5:
#         if 90 <= i <= 100:
#             print("Grade: A")
#         elif 80 <= i <= 89:
#             print("Grade: B")
#         elif 70 <= i <= 79:
#             print("Grade: C")
#         elif 60 <= i <= 69:
#             print("Grade: D")
#         else:
#             print("Grade: F")

# main()

#Prime Numbers
# def main():
#     number = int(input("Enter a number to see if its a prime number: "))
#     result = is_prime(number)
#     print(result)

# def is_prime(number):
#     if number == 2 or number % 2 != 0:
#         return True
#     else:
#         return False
# main()

#Future Value
# def main():
#     p = float(input("Enter current value: "))
#     i = float(input("Enter monthly interest rate: "))
#     t = int(input("Enter number of months: "))
#     result = future_value(p, i, t)
#     print(f"The future value is ${result:,.2f}")
        
# def future_value(p, i, t):
#         f = p * ((1 + i) ** t)
#         return f

# main()

#Number guesser
# import random

# def random_number():
#     correct_number = random.randrange(101)
#     count = 0
#     while True:
#         number = int(input("Pick a number between 1 and 100: "))
#         count += 1
#         if correct_number == number:
#             print(f"Winner! {count} attempts!")
#             print("picking a new number!")
#             count = 0
#             continue
#         elif correct_number > number:
#             print("Too low!, try again")
#         else:
#             print("Too high!, try again!")

# random_number()


#Falling_Distance
    
# def falling_distance():
#     g = 9.8
#     for t in range(1, 11):
#         d = 0.5 * g * (t ** 2)
#         print(f"{t} seconds = {d:.2f} meters")

# falling_distance()

#Odd/Even Counter
# import random

# def determine_number():
#     odd = 0
#     even = 0
#     for i in range(1, 101):
#         number = random.randint(1, 1000)
#         if number % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print('Odd count:', odd, 'Even count:', even)

# determine_number()

#Test Average and Grade
# import math

# test1 = int(input("Enter the first test grade: "))
# test2 = int(input("Enter the second test grade:"))
# test3 = int(input("Enter the third test grade: "))
# test4 = int(input("Enter the fourth test grade: "))
# test5 = int(input("Enter the fifth test grade: "))

# def calc_average(test1, test2, test3, test4, test5):
#     sum = test1 + test2 + test3 + test4 + test5
#     average = math.ceil(sum / 5)
#     return average
        
# def determine_grade(test1, test2, test3, test4, test5):
#         for i in test1, test2, test3, test4, test5:
#             if 90 <= i <= 100:
#                 print("Grade: A")
#             elif 80 <= i <= 89:
#                 print("Grade: B")
#             elif 70 <= i <= 79:
#                 print("Grade: C")
#             elif 60 <= i <= 69:
#                 print("Grade: D")
#             else:
#                 print("Grade: F")

# determine_grade(test1, test2, test3, test4, test5)
# result = calc_average(test1, test2, test3, test4, test5)
# print("The class average:", result,"%")

#Future Value
# p = float(input('Enter present value: '))
# i = float(input('Enter monthly interest: '))
# t = int(input('Enter number of months: '))
# count = 1

# def future_value(p, i, t):
#     f = p * ((1 + i) ** t)
#     return f

# for month in range(1, t + 1):
#     f = p * ((1 + i) ** month)
#     print(f"Value: ${f:,.2f} Month: {month}")

# final_value = future_value(p, i, t)
# print(f"This is the future value ${final_value:,.2f}")

#Falling_Distance

# def falling_distance(t):
#     g = 9.8
#     d = 0.5 * g * (t ** 2)
#     print(f"{d:.2f} meters in {t} seconds")

# for t in range(1, 10):
#     falling_distance(t)

#Kinetic Energy

# m = float(input("Enter the mass in kilograms: "))
# v = float(input("Enter the velocity in meters per second: "))

# def kinetic_energy(m, v):
#     ke = 0.5 * (m * (v ** 2))
#     return ke

# result = kinetic_energy(m, v)
# print(f"{result:.2f} joules")

# feet = float(input("Enter the number of feet: "))

# def feet_to_inches(feet):
#     converter = 12
#     inches = feet * converter
#     return inches

# result = feet_to_inches(feet)
# print(f"{feet} feet is equivalent to {result} inches")

# import random

# x = random.randint(1, 1000)
# y = random.randint(1, 1000)

# def math_quiz(x, y):
#     print("Solve the math problem:")
#     print(f"  {x}")
#     print(f"+ {y}")
#     answer = int(input("Solve the problem: "))
#     if answer == x + y:
#         print("Correct!")
#     else:
#         print("Incorrect!")

# math_quiz(x, y)
# import random

# def math_quiz():
#     x = random.randint(1, 1000)
#     y = random.randint(1, 1000)
#     count = 0
#     while True:
#         print("Solve the math problem:")
#         print(f"  {x}")
#         print(f"+ {y}")
#         answer = int(input("Solve the problem: "))
#         count += 1
#         if answer == x + y:
#             print(f"Correct! {count} attempts.")
#             x = random.randint(1, 1000)
#             y = random.randint(1, 1000)
#             count = 0
#             continue
#         else:
#             print("Try again!")

# math_quiz()

# Test Average and Quiz
# import math
# test1 = int(input("Enter the first test grade: "))
# test2 = int(input("Enter the second test grade: "))
# test3 = int(input("Enter the third test grade: "))
# test4 = int(input("Enter the fourth test grade: "))
# test5 = int(input("Enter the fifth test grade: "))

# def calc_average(test1, test2, test3, test4, test5):
#     sum = test1 + test2 + test3 + test4 + test5
#     average = math.ceil(sum / 5)
#     return average

# def determine_grade(test1, test2, test3, test4, test5):
#     for i in test1, test2, test3, test4, test5:
#         print(i)
#         if 90 <= i <= 100:
#             print("A")
#         elif 80 <= i <= 89:
#             print("B")
#         elif 70 <= i <= 79:
#             print("C")
#         elif 60 <= i <= 69:
#             print("D")
#         else:
#             print("F")


# result = calc_average(test1, test2, test3, test4, test5)
# print(f"Class average: {result}%")
# determine_grade(test1, test2, test3, test4, test5)

# def falling_distance(t):
#     g = 9.8
#     d = 0.5 * g * (t ** 2)
#     print(f"{d:.2f} meters in {t} seconds")

# for t in range(1, 11):
#     falling_distance(t)


#Copy data to another file
# with open('my_data.txt', 'r') as data_file, open('my_copy.txt', 'w') as copy_file:
#     for line in data_file:
#         copy_file.write(line)


# grade_file = open('grade.txt', 'r')
# passing_file = open('passing.txt', 'w')

# for line in grade_file:
#     grade = int(line.strip())
#     if grade >= 6:
#         passing_file.write(str(grade) + '\n')

# grade_file.close()
# passing_file.close()

# file_name = open('words.txt', 'r')
# count = 0

# for line in file_name:
#     if line.strip() == "sunshine":
#         count += 1

# file_name.close()

# def main():
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/numbers.txt', 'r') as file:
#         count = 0
#         total = 0
#         for line in file:
#             total += int(line)
#             count += 1
#     average = total / count
#     print(f'The average is {average}')

# main()
        
# def main():
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/numbers.txt', 'r') as main_file, open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/copy.txt', 'w') as copy_file:
#         total = 0
#         count = 0
#         for line in main_file:
#             copy_file.write(line)
#             total += int(line)
#             count += 1
#         average = total / count

#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/copy.txt', 'a') as copy_file:
#         copy_file.write(f'{average}')

#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/copy.txt', 'r') as copy_file:
#         result = copy_file.read()
    
#     print(result)
    
# main()

# with open('fahrenheit.txt', 'r') as main_file, open('celsius.txt', 'w') as copy_file:
#     try:
#         for line in main_file:
#             temp = float(line)
#             cels = (temp - 32) * (5/9)
#             copy_file.write(str(cels))

#     except InvalvidError:
#         print("Invalid Error")



# with open("numbers.txt", "r") as file:
#     negative_count = 0
#     positive_count = 0
#     negative_total = 0
#     positive_total = 0
#     for number in file:
#         number = float(number)
#         if number > 0:
#             positive_total += number
#             positive_count += 1
#         elif number < 0:
#             negative_total += number
#             negative_count += 1

# if negative_count == 0:
#     print("NaN")
# else:
#     print(negative_total/negative_count)

# if positive_count == 0:
#     print("NaN")
# else:
#     print(positive_total/positive_count)

# try:
#     with open('fahrenheit.txt', 'r') as f_file, open('celsius.txt', 'w') as c_file:
#         try:
#             for line in f_file:
#                 number = float(line)
#                 celc = (number - 32) * (5/9)
#                 c_file.write(f'{celc:.2f}\n')
#         except ValueError:
#             print("Invalid data")
# except FileNotFoundError:
#             print("File not found")


# max1 = float('-inf')
# max2 = float('-inf')

# array = [5, 20, 21, 3, 42, 21, 27, 43]

# for i in range(0, len(array)):
#     if array[i] > max1:
#         max2 = max1
#         max1 = array[i]
#     elif array[i] > max2:
#         max2 = array[i]

# print(max1, max2)

# array = [5, 20, 21, 3, 42, 21, 27, 43]

# array_sum = 0

# count = 0

# for i in range(0, len(array)):
#     array_sum += array[i]
#     if array[i] % 3 == 0:
#         count += 1
    
# print(array_sum)
# print(count)

import random
x = random.randint(1, 10)
y = random.randint(1, 10)

def math_quiz(x, y):
    print(f" {x}")
    print(f"+{y}")
    total = x + y
    count = 0
    while True:
        answer = int(input("Answer the math equation: "))
        count += 1
        if answer != total:
            print("Try Again")
            print(f" {x}")
            print(f"+{y}")
        else:
            print("Correct!")
            print(f"{count} attempts!")
            break

math_quiz(x, y)

# math_quiz(x, y)
# import random

# def math_quiz():
#     x = random.randint(1, 1000)
#     y = random.randint(1, 1000)
#     count = 0
#     while True:
#         print("Solve the math problem:")
#         print(f"  {x}")
#         print(f"+ {y}")
#         answer = int(input("Solve the problem: "))
#         count += 1
#         if answer == x + y:
#             print(f"Correct! {count} attempts.")
#             x = random.randint(1, 1000)
#             y = random.randint(1, 1000)
#             count = 0
#             continue
#         else:
#             print("Try again!")

# math_quiz()





