#Populatiom

# def main():
#     population_number = []

#     with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/uspopulation.txt", "r") as file:
#         for line in file:
#             number = int(line)
#             population_number.append(number)    
    

        
   
# # main()

# def get_values(list1, list2):
#     list3 = []
    
#     # Append all elements while avoiding duplicates
#     for num in list1 + list2:
#         if num not in list3:  # Manually checking for duplicates
#             list3.append(num)

#     list3.sort()  # Using sort() since it's allowed
#     return list3

# # Test case
# list1 = [-1, 0, 1, 2, 3, 4]
# list2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# result = get_values(list1, list2)
# print(result)

#1 Total Sales
# def main():
#     total = 0
#     count = 1
#     week = []
#     for i in range(7):
#         sales = float(input(f"Enter the sales for day #{count}: "))
#         week.append(sales)
#         count += 1
    
#     for i in week:
#         total += i

#     print(f"The total for the week is ${total:,.2f}")

# main()

#2 Lottery Number Generator
# import random

# def main():
#     lottery = []
#     for i in range(7):
#         number = random.randint(0, 9)
#         lottery.append(number)

#     print("The lottery numbers are ....")
#     print(lottery)

# main()

# def main():
#     month = 1
#     array = []
#     for i in range(12):
#         rainfall = float(input(f"Enter the amount of rain in inches on month #{month}: "))
#         array.append(rainfall)
#         month += 1
        
#     min_rain = min(array)
#     max_rain = max(array)
#     total = sum(array)
#     average = sum(array) / len(array)
#     print(f"The lowest amount of rain in a month was {min_rain}")
#     print(f"The most rain for one month was {max_rain:.2f} inches")
#     print(f"The total rainfall for the 12 months was {total:.2f} inches.")
#     print(f"The average rain fall per month was {average:.2f} inches")


# main()

#4 Number Analysis Program
# def main():
#     array = []
#     for i in range(20):
#         number = int(input("Enter a number: "))
#         array.append(number)

#     lowest_number = min(array)
#     highest_number = max(array)
#     total = sum(array)
#     average = total / len(array)
#     print(f"Lowest Number: {lowest_number}")
#     print(f"Highest Number: {highest_number}")
#     print(f"Total: {total}")
#     print(f"Average: {average}")

# main()

#6 Larger than n

def main():
    array = [5, 8, 2, 5, 6, 4, 3, 10, 7]
    number = int(input("Enter a number: "))
    result = greater_than(array, number)
    print(f"These numbers greater are {result}")

def greater_than(array, number):
    new_array = []
    for i in array:
        if number < i:
            new_array.append(i)

    return new_array

main()