monthly_inc = int(input("Enter your monthly income: "))
monthly_exp = int(input("Enter your total monthly expenses: "))
monthly_sav = monthly_inc - monthly_exp
Projected_Savings = monthly_sav * 12 + (monthly_sav * 12 * 0.05)

print(f"Your monthly savings are {monthly_sav}")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")