# Mortgage Calculator

class MortgageCalculator:
    def __init__(self, principal, interest_rate, loan_term):
        self.principal = principal
        self.interest_rate = interest_rate
        self.loan_term = loan_term

    def calculate_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 12
        num_payments = self.loan_term * 12
        monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
        return round(monthly_payment, 2)

    def calculate_total_interest_paid(self):
        monthly_payment = self.calculate_monthly_payment()
        num_payments = self.loan_term * 12
        total_interest_paid = (monthly_payment * num_payments) - self.principal
        return round(total_interest_paid, 2)


principal = float(input("Enter the loan amount: $"))
interest_rate = float(input("Enter the annual interest rate (%): ")) / 100
loan_term = int(input("Enter the loan term (in years): "))

mortgage_calculator = MortgageCalculator(principal, interest_rate, loan_term)

monthly_payment = mortgage_calculator.calculate_monthly_payment()
total_interest_paid = mortgage_calculator.calculate_total_interest_paid()
print("\n")
print("Monthly Payment: $", monthly_payment, "\n")
print("Total Interest Paid: $", total_interest_paid, "\n")


