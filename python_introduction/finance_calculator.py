monthly_inc = int(input("Enter your monthly income:"))
monthly_exp = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_inc - monthly_exp
annu_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $", annu_Savings)
