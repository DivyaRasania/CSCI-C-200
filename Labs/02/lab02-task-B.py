restaurant_bill = float(input("Enter your bill amount: "))

fifteen_percent_tip = restaurant_bill * 0.15
twenty_percent_tip = restaurant_bill * 0.2

final_fifteen_percent_bill = fifteen_percent_tip + restaurant_bill
final_twenty_percent_bill = twenty_percent_tip + restaurant_bill

print(f"15% tip: ${fifteen_percent_tip} and total bill will be: ${final_fifteen_percent_bill}")
print(f"20% tip: ${twenty_percent_tip} and total bill will be: ${final_twenty_percent_bill}")
