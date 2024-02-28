TAX = 0.07
TIP = 0.18
basic_charge = float(input("Please input charge for the food: $"))

tax_amount = basic_charge * TAX
tip_amount = basic_charge * TIP
total = basic_charge + tax_amount + tip_amount

tax_amount_formatted = "{:.2f}".format(tax_amount)
tip_amount_formatted = "{:.2f}".format(tip_amount)
total_formatted = "{:.2f}".format(total)

print("The tax amount is: $", tax_amount_formatted)
print("The tip amount is: $", tip_amount_formatted)
print("The total is: $", total_formatted)
