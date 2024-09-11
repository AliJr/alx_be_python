monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your montly savings are $", monthly_savings)
print("Projected savings after one year, with intrester, is:", savings)
