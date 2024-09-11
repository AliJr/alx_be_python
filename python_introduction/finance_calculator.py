income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expense
savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Your montly savings are", monthly_savings)
print("Projected savings after one year, with intrester, is:", savings)
