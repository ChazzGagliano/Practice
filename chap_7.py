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
#     print(f"Average: {average:.2f}")

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

# def main():
#     rain_stats()

# def rain_stats():
#     count = 1
#     year = []
#     for i in range(12):
#         rain = float(input(f"Enter the inches of rain on month #{count}: "))
#         year.append(rain)
#         count += 1

#     print(year)
#     highest_month = 0
#     lowest_month = 0
#     max_rain = year[0]
#     min_rain = year[0]
#     for i in range(len(year)):
#         if year[i] > max_rain:
#             max_rain = year[i]
#             highest_month = i + 1
#         elif year[i] < min_rain:
#             min_rain = year[i]
#             lowest_month = i + 1
    
#     print(lowest_month)
#     print(highest_month)
#     print(sum(year))
#     average = sum(year) / len(year)
#     print(f"{average:2f}")
 


# main()

#5 Charge Account Validation

# def main():
#     try:
#         accounts = []
#         with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/charge_accounts.txt", "r") as file:
#             for line in file:
#                 number = int(line)
#                 accounts.append(number)

#             numbers = int(input("Enter you seven digit account: "))
#             if numbers in accounts:
#                 print("The number is valid")
#             else:
#                 print("The number is not valid")

#     except FileNotFoundError:
#         print("file not found")

# main()

# def main():
#     try:
#         array = ['Yes, of course!', 'Without a doubt, yes.', 'You can count on it.', 'For sure!', 'Ask me later.', "I'm not sure.", "I can't tell right now.", "I'll tell you after my nap.", 'No way!', "I don't think so.", 'Without a doubt, no.', 'The answer is clearly NO.']
#         with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/copy.txt", "w") as file:
#             for i in array:
#                 file.write(f"{i}\n")
            

#     except FileNotFoundError:
#         print("File not Found")
# main()

# array = [1, 20, 4, 2, 6, 7, 8]
# max_product = array[0] * array[1]
# min_product = array[0] * array[1]


# for i in range(1, len(array)):
#     product = array[i] * array[i - 1]
#     if product > max_product:
#         max_product = product
#     elif product < min_product:
#         min_product = product 

# print(max_product)
# print(min_product)

# def main():
#     try:
#         population = []
#         with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/uspopulation.txt", "r") as file:
#             for line in file:
#                 number = int(line)
#                 population.append(number)

#         increase = []
#         for i in range(1, len(population)):
#             yearly_population = population[i] - population[i - 1]
#             increase.append(yearly_population)

#         max_increase = increase[0]
#         min_increase = increase[0]
#         first_year = 1951
#         total = 0
#         for i in range(len(increase)):
#             if increase[i] > max_increase:
#                 max_increase = increase[i]
#                 highest_year = first_year + i 
#             if increase[i] < min_increase:
#                 min_increase = increase[i]
#                 lowest_year = first_year + i 
#             total += increase[i]
        
#         average = total / len(increase)

#         print(f"The average annual change in population during the time period was {average:.2f}.")
#         print(f"The year with the greatest increase in population during the time period was {highest_year}.")
#         print(f"The year with the lowest increase in population during the time period was {lowest_year}.")

#     except FileNotFoundError:
#         print("File Not Found")
# main()

#10 World Series Champions
# def main():
#     with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/worldserieswinners.txt", "r") as file:
#         team = input("Enter a team: ")
#         count = 0
#         for line in file:
#             line = line.strip()
#             if team == line:
#                 count += 1

#         if count == 0:
#             print("This team has never won a world series.")
#         elif count == 1:
#             print(f"This team has only won a single world series.")
#         else:
#             print(f"This team has won {count} times.")
            
# main()

#8 Name Search
# def main():
#     try:
#         with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/boynames.txt", "r") as file:
#             names = []
#             for line in file:
#                 line = line.strip()
#                 names.append(line)

#             name = input("Enter a name: ")
#             name = name.capitalize()
#             if name in names:
#                 print("This was a popular name from the year 2000 to 2009")
#             else:
#                 print("This was not a popular name from the year 2000 to 2009")


#     except FileNotFoundError:
#         print("File not found")


# main()

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

#Larger than n
# def main():
#     n = int(input("Enter a number: "))
#     numbers = [1, 5, 8, 2, 10, 12, -1]
#     larger_than(n, numbers)

# def larger_than(n, numbers):
#     new_list = []
#     for i in range (0, len(numbers)):
#         if numbers[i] > n:
#             new_list.append(numbers[i])
#     if new_list == []:
#         print("There are no numbers in the list greater.")
#     else:
#         print(f"These are numbers greater than {n}: {new_list}")



# main()

#Two Max Numbers
# def main():
#     numbers = [1, 5, 12, 8, 27, 32, 15]
#     max1 = numbers[0]
#     max2 = numbers[0]

#     for i in range(0, len(numbers)):
#         if numbers[i] > max1:
#             max2 = max1
#             max1 = numbers[i]

#         elif numbers[i] > max2:
#             max2 = numbers[i]
#     print(max1)
#     print(max2)

# main()



# def main():
#     number = 0
#     location = 0
#     array = [6, 7, 8, 9, 10]

#     for i in range (0, len(array)):
#         array.insert(location, number)
#         number += 1
#         location += 1
#     print(array)


# main()

# def main():
#     array = [1, 5, 50, 7, 27, 13, 40]
#     max1 = array[0]
#     max2 = array[0]
#     highest_number(array, max1, max2)


# def highest_number(array, max1, max2):
#     for i in range(0, len(array)):
#         if array[i] > max2:
#             max1 = max2
#             max2 = array[i]
#         elif array[i] > max1:
#             max1 = array[i]

#     print(max2, max1)



# main()



# def main():
#     correct_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#     wrong_questions = []
#     count = 0
#     index = 0
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/answers.txt', 'r') as file:
#         for line in file:
#             line = line.strip()
#             if line == correct_list[index]:
#                 count += 1
#             else:
#                 wrong_questions.append(index + 1)
#             index += 1


#         if count >= 15:
#             print(f'Congrats! You got {count} out of 20 questions right! You got {len(wrong_questions)} questions wrong, These were the incorrect questions: {wrong_questions}')
        
#         else:
#             print(f'Sorry you got {count} out of 20 which means you failed. You got {len(wrong_questions)} questions wrong, These are the questions you got wrong: {wrong_questions}')
        

# main()

# def main():
#     string_input = input("Enter a string")
#     result = string_function(string_input)
#     print(result)

# def string_function(string_input):
#     count = 0
#     vowels = "aeiou"
#     for i in range(0, len(string_input)):
#         if string_input[i] in vowels:
#             count += 1

#     return count

# main()

def main():
    string_one = "hello world this is a test hello this"
    string_two = "hello test"
    common_word_count(string_one, string_two)

def common_word_count(string_one, string_two):
    word_one = string_one.split()
    word_two = string_two.split()

    word_count = {}

    for word in word_one:
        if word in word_two:
            count_one = word_one.count(word)
            count_two = word_two.count(word)
            word_count[word] = count_one + count_two
        
    print(word_count)

main()