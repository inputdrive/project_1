# Mortgage Calculator

principal = float(input("Enter the loan amount: $"))

interest_rate = float(input("Enter the annual interest rate (%): ")) / 100
loan_term = int(input("Enter the loan term (in years): "))

monthly_interest_rate = interest_rate / 12
num_payments = loan_term * 12
monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
total_interest_paid = (monthly_payment * num_payments) - principal

print("\n","Monthly Payment: $", round(monthly_payment, 2), "\n")

print("Total Interest Paid: $", round(total_interest_paid, 2), "\n")
