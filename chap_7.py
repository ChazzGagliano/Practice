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

#11 Lo Shu Magic Square
# def main():
#     two_dim_square = [
#         [4, 9, 2],
#         [3, 5, 7],
#         [8, 1, 6],
#     ]
#     two_d(two_dim_square)

# def two_d(two_dim_square):
#     if sum(two_dim_square[0]) == 15 and sum(two_dim_square[1]) == 15 and sum(two_dim_square[2]) == 15 and (two_dim_square[0][0] + two_dim_square[1][0] + two_dim_square[2][0]) == 15 and (two_dim_square[0][1] + two_dim_square[1][1] + two_dim_square[2][1]) == 15  and (two_dim_square[0][2] + two_dim_square[1][2] + two_dim_square[2][2]) == 15 and (two_dim_square[0][0] + two_dim_square[1][1] + two_dim_square[2][2]) == 15 and (two_dim_square[2][0] + two_dim_square[1][1] + two_dim_square[0][2]) == 15:
#         print("This is a Lo Shu Magic square!")
#     else:
#         print("Not a Lo Shu Magic square!")

# main()

#13 Magic 8 ball
# import random

# def main():
#     try:
#         response = []
#         with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/8_ball.txt", "r") as file:
#             for line in file:
#                 response.append(line.strip())

#         while True:
#             question = input("Ask a question!(Enter 'exit' to quit): ")
#             if question == "exit":
#                 print("Goodbye!")
#                 break
#             i = random.randint(0, 11)
#             print(response[i])
#     except FileNotFoundError:
#         print("File not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# main()

# def main():
#     numbers = [5, 8, 9, 31, 27, 3]
#     n = 3
#     multiple_o_n(numbers, n)

# def multiple_o_n(numbers, n):
#     new_list = []
#     for i in range(len(numbers)):
#         if numbers[i] % n == 0:
#             new_list.append(numbers[i])
#     print(new_list)


# main()

#Lottery
# import random

# lottery = []

# for i in range(7):
#     number = random.randint(0, 9)
#     lottery.append(number)

# print(lottery)

#Sales
# def main():
#     week_sales()

# def week_sales():
#     week = []
#     day = 1
#     total = 0
#     for i in range(7):
#         sales = float(input(f"Enter the sales for day #{day}: "))
#         week.append(sales)
#         day += 1
#         total += sales
#     print(week)
#     print(f"${total:,.2f}")
# main()

def main():
    rain_stats()

def rain_stats():
    count = 1
    year = []
    for i in range(12):
        rain = float(input(f"Enter the inches of rain on month #{count}: "))
        year.append(rain)
        count += 1

    print(year)
    highest_month = 0
    lowest_month = 0
    max_rain = year[0]
    min_rain = year[0]
    for i in range(len(year)):
        if year[i] > max_rain:
            max_rain = year[i]
            highest_month = i + 1
        elif year[i] < min_rain:
            min_rain = year[i]
            lowest_month = i + 1
    
    print(lowest_month)
    print(highest_month)
    print(sum(year))
    average = sum(year) / len(year)
    print(f"{average:2f}")
 


main()