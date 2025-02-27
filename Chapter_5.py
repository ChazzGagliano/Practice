#1 Kilometer Converter
# km = int(input("Enter the amount in kilometers: "))

# def kilometer_converter(km):
#     miles = km * 0.6214
#     print(f"{km} kilometers is equivalnet to {result:.2f} miles")

# kilometer_converter(km)

#2 Sales Tax Refactoring
# def main():
#     sale = float(input("Enter value for sale: "))
#     result = tax_refactoring(sale)
#     print(f'The total for the sale is ${result:.2f}')

# def tax_refactoring(sale):
#     county_tax = sale * .03
#     state_tax = sale * .05
#     total = sale + county_tax + state_tax
#     return total

# main()

#3 How much insurance?
def main():
    cost = float(input("Enter replacement cost of building: "))
    result = insurance_cost(cost)
    print(f"The minimum cost of insurance would be ${result:,.2f}")

def insurance_cost(cost):
    insurance = cost * 0.80
    return insurance

main()
