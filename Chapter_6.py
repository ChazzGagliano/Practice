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


#1 File Display
# def main():
#     file = input('enter the file name: ')
#     file_path = f'/Users/chazzgagliano/Desktop/CSC106/CSC106Python/{file}'
#     with open(file_path, 'r') as i:
#         for line in i:
#             number = int(line)
#             print(number)

# main()

# #2 File Head Displai

# def main():
#     file = input("Enter name of file: ")
#     file_path = f'/Users/chazzgagliano/Desktop/CSC106/CSC106Python/{file}'
#     with open(file_path, "r") as i:
#         count = 0
#         for line in i:
#             if count == 5:
#                 break
    
#             if line.strip():
#                 print(line.strip())
#                 count += 1 
#             else:
#                 count += 5

# main()

#3 Line numbers

# def main():
#     file = input("Enter name of file: ")
#     file_path = f'/Users/chazzgagliano/Desktop/CSC106/CSC106Python/{file}'
#     with open(file_path, 'r') as f:
#         count = 1
#         for line in f:
#             if line.strip():
#                 print(f"{count}: {line.strip()}")
#                 count += 1
#             else:
#                 break
                


# main()

#4 Item counter:
# def main():
#     try:
#         with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/names.txt', 'r') as file:
#             count = 0
#             for line in file:
#                 if line != '':
#                     count += 1
#                 else:
#                     break
#             print(f"{count} names in file.")

#     except FileNotFoundError:
#         print("File not Found")


# main()

#5 Sum of numbers
# def main():
#     try:
#         with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/numbers.txt', 'r') as file:
#             total = 0
#             for line in file:
#                 if line != '':
#                     number = int(line)
#                     total += number
#                 else:
#                     break
#             print(total)
#     except FileNotFoundError:
#         print("File not found")
    
# main()

#7 Random Number File Writer
# import random

# def main():
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/random.txt', 'w') as file:
#         times = int(input("Enter the amount of numbers in the file: "))
#         for i in range(times):
#             number = random.randint(1, 500)
#             file.write(f'{number}\n')

#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/random.txt', 'r') as file:
#         for line in file:
#             print(line.strip())

# main()

#8 Random Number File Reader
# import random

# def main():
#     with open('/Users/chazzgagliano/Desktop/CSC106/CSC106Python/random.txt', 'r') as file:
#         total = 0
#         count = 0
#         for line in file:
#             number = int(line)
#             total += number
#             count += 1
#         print(f'There are {count} numbers in the file and the total is {total}.')


# main()

#11 Personal Web Page Generator

# def main():
#     name = input("Enter your name: ")
#     description = input("Describe yourself: ")
#     with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/random.txt", "w") as file:
#         file.write(f"<html>\n<head>\n</head>\n<body>\n  <center>\n    <h1>{name}</h1>\n  </center>\n<hr />\n{description}\n<hr />\n</body>\n</html>")

#     with open("/Users/chazzgagliano/Desktop/CSC106/CSC106Python/random.txt", "r") as file:
#         for line in file:
#             print(line)
# main()











