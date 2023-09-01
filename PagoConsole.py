
from Pago import DeudaTarjetaCredito

print("This program allows you to calculate the fee to be paid for a credit card purchase")
amount = float( input("Purchase amount:") )
interest = float( input("Card interest rate:") )
payment = int(input("Numero de cuotas en que va a diferir la compra:"))

deuda = DeudaTarjetaCredito(amount, interest, payment)

print("Cuota mensual:", deuda.monthly_payment)
print("Intereses totales a pagar:", deuda.calculate_monthly_payment())

plan_amortizacion = deuda.calculate_amortization_plan()
print("\nPlan de amortización:")
for monthly_payment, interest_payment, main_payment, remaining_fund in plan_amortizacion:
    print(f"Cuota: {monthly_payment:.2f} | Interés: {interest_payment:.2f} | Principal: {main_payment:.2f} | Saldo restante: {remaining_fund:.2f}")

num_cuota_abono = int(input("\nIngrese el número de cuota para abonar extra: "))
monto_abono = float(input("Ingrese el monto a abonar extra: "))
plan_with_extra = deuda.calculate_extra_payment(monto_abono, num_cuota_abono)

print("\nPlan de amortización con abono extra:")
for monthly_payment, interest_payment, main_payment, remaining_fund in plan_with_extra:
    print(f"Cuota: {monthly_payment:.2f} | Interés: {interest_payment:.2f} | Principal: {main_payment:.2f} | Saldo restante: {remaining_fund:.2f}")
