def add_tax(costs, tax):
    tax_value = (1 + tax)
    for cost in costs:    
        tax_value = round((cost * tax_value), 2)    
    return tax_value

number_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

name_list = []
cost_list = []

i = 0
while i < number_purchases: 
    name = input("Customer: ")
    cost = float(input("Cost: "))
    name_list.append(name)
    cost_list.append({cost})
    i += 1

tax_list = []
i = 0
while i < len(cost_list):
    final_value = add_tax(cost_list[i], sales_tax)
    tax_list.append(final_value)
    i += 1

prices = tax_list
customers = name_list

print(prices)
print(customers)


# two conditions

statements = {}

for key in customers:
    for value in prices:
        statements[key] = value
        prices.remove(value)
        break
print(statements)