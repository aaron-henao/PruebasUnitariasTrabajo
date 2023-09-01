class DeudaTarjetaCredito:
    def __init__(self, amount, interest, payment):
        # Verificamos las entradas para evitar valores inválidos
        if amount <= 0:
            raise ValueError("Error el Monto debe ser superior a cero")
        if payment <= 0:
            raise ValueError("Error: El numero de cuotas debe ser mayor a cero")
        if interest > 100:
            raise ValueError("Error: La Tasa anual de interes supera el 100%")

        self.amount = amount
        self.interest = interest / 100
        self.payment = payment
        self.monthly_payment = self.calculate_monthly_payment()  # Calculamos la cuota mensual

    # Método para calcular el total de intereses a pagar
    def calculate_total_interest(self):
        total_interest = 0  # Inicializamos el total de intereses
        if self.interest == 0:
            return total_interest
        elif self.payment == 1:
            return total_interest
        else:
            remaining_fund = self.amount  # Inicializamos el saldo restante
            for _ in range(self.payment):
                interest_payment = remaining_fund * self.interest  # Calculamos el pago de intereses
                total_interest += interest_payment  # Sumamos el pago de intereses al total
                remaining_fund -= self.monthly_payment - interest_payment  # Actualizamos el saldo restante
            return total_interest  # Devolvemos el total de intereses

    # Método para calcular la cuota mensual basada en la fórmula de amortización
    def calculate_monthly_payment(self):
        if self.interest == 0:
            return self.amount / self.payment
        else:
            # Aplicamos la fórmula de amortización para calcular la cuota mensual
            return (self.amount * self.interest) / (1 - (1 + self.interest) ** (-self.payment))

    # Método para calcular el plan de amortización
    def calculate_amortization_plan(self):
        plan = []  # Inicializamos la lista para el plan de amortización
        remaining_fund = self.amount  # Inicializamos el saldo restante
        for _ in range(self.payment):
            interest_payment = remaining_fund * self.interest  # Calculamos el pago de intereses
            main_payment = self.monthly_payment - interest_payment  # Calculamos el pago a principal
            # Agregamos la información de la cuota al plan de amortización
            plan.append((self.monthly_payment, interest_payment, main_payment, remaining_fund))
            remaining_fund -= main_payment  # Actualizamos el saldo restante
        return plan  # Devolvemos el plan de amortización

    # Método para calcular el efecto de un pago extra en una cuota específica

    def calculate_extra_payment(self, extra_payment, payment_number):
        if payment_number < 1 or payment_number > self.payment:
            raise ValueError("Número de cuota inválido")

        plan = self.calculate_amortization_plan()
        plan_with_extra = []

        for i, (monthly_payment, interest_payment, main_payment, remaining_fund) in enumerate(plan):
            if i + 1 == payment_number:
                if extra_payment <= 0:
                    raise ValueError("Error, el abono debe ser superior a cero")
                if extra_payment < monthly_payment:
                    raise ValueError("Error, el abono debe ser igual o menor a la cuota calculada")
                main_payment = extra_payment - monthly_payment
                remaining_fund = remaining_fund - main_payment
                monthly_payment = extra_payment
            plan_with_extra.append((monthly_payment, interest_payment, main_payment, remaining_fund))

        return plan_with_extra
