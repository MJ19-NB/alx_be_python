monthly_income = float(ipunt('Enter your monthly income:'))
monthly_expenses = float(input('Enter your monthly expenses'))
monthly_savings = monthly_income - monthly_expenses
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year,with intrest, is: $",annual_savings)