
from Payment import PaymentCreditCard

print("This program allows you to calculate the fee to be paid for a credit card purchase")
amount = float( input("Purchase amount:") )
interest = float( input("Card interest rate:") )
payment = int(input("Number of installments in which the purchase will be deferred:"))

debt = PaymentCreditCard(amount, interest, payment)

print("Monthly payment:", debt.monthly_payment)
print("Total interest:", debt.calculate_monthly_payment())

amortization_plan = debt.calculate_amortization_plan()
print("\nAmortization plan:")
for monthly_payment, interest_payment, main_payment, remaining_fund in amortization_plan:
    print(f"Payment: {monthly_payment:.2f} | Interest: {interest_payment:.2f} |Main payment: {main_payment:.2f} | Remaining fund: {remaining_fund:.2f}")

number_payment_extra = int(input("\nEnter the fee number to pay extra:"))
extra = float(input("Enter the amount to pay extra:"))
plan_with_extra = debt.calculate_extra_payment(extra, number_payment_extra)

print("\nAmortization plan with extra payment:")
for monthly_payment, interest_payment, main_payment, remaining_fund in plan_with_extra:
    print(f"Payment: {monthly_payment:.2f} | Interest: {interest_payment:.2f} |Main payment: {main_payment:.2f} | Remaining fund: {remaining_fund:.2f}")
