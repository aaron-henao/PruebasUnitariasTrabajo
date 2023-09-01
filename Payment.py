class PaymentCreditCard:
    def __init__(self, amount, interest, payment):
        # We check the entries to avoid invalid values
        # Verificamos las entradas para evitar valores inválidos
        if amount <= 0:
            raise ValueError("Error: Amount must be greater than zero")
        if payment <= 0:
            raise ValueError("Error: The number of quotas must be greater than zero")
        if interest > 100:
            raise ValueError("Error: Annual interest rate exceeds 100%")

        self.amount = amount
        self.interest = interest / 100
        self.payment = payment
        self.monthly_payment = self.calculate_monthly_payment()  # Calculate monthly payment
                                                                # Calculamos la cuota mensual

    # Method for calculating the total interest payable
    # Método para calcular el total de intereses a pagar
    def calculate_total_interest(self):
        total_interest = 0  # We initialize the total interest -  Inicializamos el total de intereses
        if self.interest == 0:
            return total_interest
        elif self.payment == 1:
            return total_interest
        else:
            remaining_fund = self.amount  # We initialize the remaining balance - Inicializamos el saldo restante
            for _ in range(self.payment):
                interest_payment = remaining_fund * self.interest  # We calculate the interest payment - Calculamos el pago de intereses
                total_interest += interest_payment  # We add the interest payment to the total - Sumamos el pago de intereses al total
                remaining_fund -= self.monthly_payment - interest_payment  # We update the remaining balance - Actualizamos el saldo restante
            return total_interest  # We return the total interest - Devolvemos el total de intereses

    # Method for calculating the monthly installment based on the amortization formula
    # Método para calcular la cuota mensual basada en la fórmula de amortización
    def calculate_monthly_payment(self):
        if self.interest == 0:
            return self.amount / self.payment
        else:
            # We apply the amortization formula to calculate the monthly
            # Aplicamos la fórmula de amortización para calcular la cuota mensual
            return (self.amount * self.interest) / (1 - (1 + self.interest) ** (-self.payment))

    # Method for calculating the depreciation plan
    # Método para calcular el plan de amortización
    def calculate_amortization_plan(self):
        plan = []  # We initialize the list for the amortization plan - Inicializamos la lista para el plan de
        # amortización
        remaining_fund = self.amount  # We initialize the remaining balance - Inicializamos el saldo restante
        for _ in range(self.payment):
            interest_payment = remaining_fund * self.interest  # We calculate the interest payment - Calculamos el pago de intereses
            main_payment = self.monthly_payment - interest_payment  # We calculate the main payment - Calculamos el pago principal
            # We add the payment information to the amortization plan
            # Agregamos la información de la cuota al plan de amortización
            plan.append((self.monthly_payment, interest_payment, main_payment, remaining_fund))
            remaining_fund -= main_payment  # We update the remaining balance - Actualizamos el saldo restante
        return plan  # We return the amortization plan - Devolvemos el plan de amortización

    # Method for calculating the effect of an extra payment on a specific installment
    # Método para calcular el efecto de un pago extra en una cuota específica

    def calculate_extra_payment(self, extra_payment, payment_number):
        if payment_number < 1 or payment_number > self.payment:
            raise ValueError("Invalid quota number")

        plan = self.calculate_amortization_plan()
        plan_with_extra = []

        for i, (monthly_payment, interest_payment, main_payment, remaining_fund) in enumerate(plan):
            if i + 1 == payment_number:
                if extra_payment <= 0:
                    raise ValueError("Error, the subscription must be greater than zero")
                if extra_payment < monthly_payment:
                    raise ValueError("Error, the payment must be equal to or less than the calculated fee")
                main_payment = extra_payment - monthly_payment
                remaining_fund = remaining_fund - main_payment
                monthly_payment = extra_payment
            plan_with_extra.append((monthly_payment, interest_payment, main_payment, remaining_fund))

        return plan_with_extra
