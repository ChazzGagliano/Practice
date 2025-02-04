# pi = 3.141592653589793238462643383279502884197
# print(f"{pi:.2f}")
# num = pi * 10
# print(f"{num:.2f}")
# num2 = pi * 10000
# print(f"{num2:,.2f}")

#Magic Date Problem

month = int(input("Enter a month(numeric form)"))
day = int(input("Enter a day(numeric form)"))
year = int(input("Enter a year(last two digits"))

print(f"{month}/{day}/{year}")

if month * day == year:
    print("The date is magic")
else: 
    print("The date is not magic")


