
from Pago import DeudaTarjetaCredito

print("Este programa le permite calcular la cuota a pagar por una compra con tarjeta de credito")
monto_compra = float( input("Monto de la compra:") )
tasa_interes = float( input("Tasa de interés de la tarjeta:") )
num_cuotas = int( input("Numero de cuotas en que va a diferir la compra:") )

deuda = DeudaTarjetaCredito(monto_compra, tasa_interes, num_cuotas)

print("Cuota mensual:", deuda.cuota_mensual)
print("Intereses totales a pagar:", deuda.calcular_intereses_totales())

plan_amortizacion = deuda.calcular_plan_amortizacion()
print("\nPlan de amortización:")
for cuota, interes, principal, saldo in plan_amortizacion:
    print(f"Cuota: {cuota:.2f} | Interés: {interes:.2f} | Principal: {principal:.2f} | Saldo restante: {saldo:.2f}")

num_cuota_abono = int(input("\nIngrese el número de cuota para abonar extra: "))
monto_abono = float(input("Ingrese el monto a abonar extra: "))
plan_con_abono = deuda.calcular_efecto_abono_extra(monto_abono, num_cuota_abono)

print("\nPlan de amortización con abono extra:")
for cuota, interes, principal, saldo in plan_con_abono:
    print(f"Cuota: {cuota:.2f} | Interés: {interes:.2f} | Principal: {principal:.2f} | Saldo restante: {saldo:.2f}")
