class DeudaTarjetaCredito:
    def __init__(self, monto_compra, tasa_interes, num_cuotas):
        # Verificamos las entradas para evitar valores inválidos
        if monto_compra <= 0:
            raise ValueError("Error el Monto debe ser superior a cero")
        if num_cuotas <= 0:
            raise ValueError("Error: El numero de cuotas debe ser mayor a cero")
        if tasa_interes > 100:
            raise ValueError("Error: La Tasa anual de interes supera el 100%")

        self.monto_compra = monto_compra
        self.tasa_interes = tasa_interes / 100
        self.num_cuotas = num_cuotas
        self.cuota_mensual = self.calcular_cuota_mensual()  # Calculamos la cuota mensual

# Método para calcular el total de intereses a pagar
    def calcular_intereses_totales(self):
        intereses_totales = 0  # Inicializamos el total de intereses
        if self.tasa_interes == 0:
            return intereses_totales
        elif self.num_cuotas == 1:
            return intereses_totales
        else:
            saldo_restante = self.monto_compra  # Inicializamos el saldo restante
            for _ in range(self.num_cuotas):
                pago_interes = saldo_restante * self.tasa_interes  # Calculamos el pago de intereses
                intereses_totales += pago_interes  # Sumamos el pago de intereses al total
                saldo_restante -= self.cuota_mensual - pago_interes  # Actualizamos el saldo restante
            return intereses_totales  # Devolvemos el total de intereses

    # Método para calcular la cuota mensual basada en la fórmula de amortización
    def calcular_cuota_mensual(self):
        if self.tasa_interes == 0:
            return self.monto_compra / self.num_cuotas
        else:
            # Aplicamos la fórmula de amortización para calcular la cuota mensual
            return (self.monto_compra * self.tasa_interes) / (1 - (1 + self.tasa_interes) ** (-self.num_cuotas))

    # Método para calcular el plan de amortización
    def calcular_plan_amortizacion(self):
        plan = []  # Inicializamos la lista para el plan de amortización
        saldo_restante = self.monto_compra  # Inicializamos el saldo restante
        for _ in range(self.num_cuotas):
            pago_interes = saldo_restante * self.tasa_interes  # Calculamos el pago de intereses
            pago_principal = self.cuota_mensual - pago_interes  # Calculamos el pago a principal
            # Agregamos la información de la cuota al plan de amortización
            plan.append((self.cuota_mensual, pago_interes, pago_principal, saldo_restante))
            saldo_restante -= pago_principal  # Actualizamos el saldo restante
        return plan  # Devolvemos el plan de amortización

    # Método para calcular el efecto de un pago extra en una cuota específica

    def calcular_efecto_abono_extra(self, monto_abono, numero_cuota):
        if numero_cuota < 1 or numero_cuota > self.num_cuotas:
            raise ValueError("Número de cuota inválido")

        plan = self.calcular_plan_amortizacion()
        plan_con_abono = []

        for i, (cuota, interes, principal, saldo) in enumerate(plan):
            if i + 1 == numero_cuota:
                if monto_abono <= 0:
                    raise ValueError("Error, el abono debe ser superior a cero")
                if monto_abono > cuota:
                    raise ValueError("Error, el abono debe ser igual o menor a la cuota calculada")
                principal += monto_abono
                cuota -= monto_abono
            plan_con_abono.append((cuota, interes, principal, saldo))

        return plan_con_abono
