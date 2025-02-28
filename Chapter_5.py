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
# def main():
#     cost = float(input("Enter replacement cost of building: "))
#     result = insurance_cost(cost)
#     print(f"The minimum cost of insurance would be ${result:,.2f}")

# def insurance_cost(cost):
#     insurance = cost * 0.80
#     return insurance

# main()

#4 Automobile costs
# def main():
#     loan = float(input("Enter monthly loan payment: "))
#     insurance = float(input("Enter monthly insurance payment: "))
#     gas = float(input("Enter monthly gas payment: "))
#     oil = float(input("Enter monthly oil payment: "))
#     tires = float(input("Enter monthly tires payment: "))
#     maintenance = float(input("Enter montly maintenance payment: "))
#     automobile_cost(loan, insurance, gas, oil, tires, maintenance)

# def automobile_cost(loan, insurance, gas, oil, tires, maintenance):
#     monthly_cost = loan + insurance + gas + oil + tires + maintenance
#     annual_cost = monthly_cost * 12
#     print(f"The monthly cost of the automobile is ${monthly_cost:,.2f}")
#     print(f"The annual cost of the automobile is ${annual_cost:,.2f}")

# main()

#5 Property Tax
# def main():
#     property_value = float(input("Enter value of propery: "))
#     tax(property_value)

# def tax(property_value):
#     assessment_value = property_value * .60
#     property_tax = (assessment_value/100) * .72
#     print(f"The property tax for the assessment value of ${assessment_value:,.2f} is ${property_tax:,.2f}.")

# main()
