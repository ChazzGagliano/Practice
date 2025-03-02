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
def main():
    total = 0
    count = 1
    week = []
    for i in range(7):
        sales = float(input(f"Enter the sales for day #{count}: "))
        week.append(sales)
        count += 1
    
    for i in week:
        total += i

    print(f"The total for the week is ${total:,.2f}")

main()