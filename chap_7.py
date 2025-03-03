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



# 6 Larger than n

# def main():
#     array = [5, 8, 2, 5, 6, 4, 3, 10, 7]
#     number = int(input("Enter a number: "))
#     result = greater_than(array, number)
#     print(f"These numbers greater are {result}")

# def greater_than(array, number):
#     new_array = []
#     for i in array:
#         if number < i:
#             new_array.append(i)

#     return new_array

# main()

#7 Driver License Exam
# def main():
#     right_answers = 0
#     correct_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#     wrong_questions = []
#     index = 0
#     question_number = 1
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/answers.txt', 'r') as file:
#         for i in file:
#             if correct_list[index] == i.strip():
#                 right_answers += 1
#             elif correct_list != i.strip():
#                 wrong_questions.append(question_number)
#             index += 1
#             question_number += 1

#     if right_answers > 15:
#         print(f"You passed! you got {right_answers} right answers! You got {len(wrong_questions)} questions wrong. these are the questions you got wrong {wrong_questions}")
#     else:
#         print(f"Unfortunately you didnt pass. Your score was {score}%, these are the questions you got wrong{wrong_questions}")

# main()

#9 Population Data
# def main():
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/USPopulation.txt', 'r') as file:
#         data = []
#         change = []
#         for line in file:
#             number = int(line)
#             data.append(number)

#         for i in range(1, len(data)):
#             change.append(data[i] - data[i - 1])
        
#     max_change = change[0]
#     min_change = change[0]
#     first_comp = 1951
#     max_year = first_comp
#     min_year = first_comp
#     for i in range(1, len(change)):
#         if change[i] > max_change:
#             max_change = change[i]
#             max_year = first_comp + i 
#         elif change[i] < min_change:
#             min_change = change[i]
#             min_year = first_comp + i

#     average = sum(change) / len(change)
#     print(f"The average annual change in population in the time period {average:.2f}.")
#     print(f"The year with the greatest increase in population is {max_year}.")
#     print(f"The year with the lowest increase in population is {min_year}.")

# main()

# array = [1, 44, 37, 66, 8, 10, -1]
# min_number = array[0]
# max_number = array[0]

# for i in range(0, len(array)):
#     if array[i] > max_number:
#         max_number = array[i]
#     elif array[i] < min_number:
#         min_number = array[i]

# print(f"{sum(array) / len(array)}")
# print(f"{max_number}")
# print(f"{min_number}")
