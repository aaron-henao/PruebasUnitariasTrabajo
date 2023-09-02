import unittest
from Payment import PaymentCreditCard


class TestPayment(unittest.TestCase):

    # Casos de prueba para la responsabilidad R1: calcular_intereses_totales
    def test_calculate_total_interest_normal_case(self):
        Payment = PaymentCreditCard(200000, 3.1, 36)
        self.assertAlmostEqual(Payment.calculate_total_interest(), 134726.53, places=2)

    def test_calculate_total_interest_normal_case_2(self):
        Payment = PaymentCreditCard(850000, 3.4, 24)
        self.assertAlmostEqual(Payment.calculate_total_interest(), 407059.97, places=2)

    def test_calculate_total_interest_zero_rate(self):
        Payment = PaymentCreditCard(480000, 0, 48)
        self.assertAlmostEqual(Payment.calculate_total_interest(), 0, places=2)

    def test_calculate_total_interest_usury(self):
        Payment = PaymentCreditCard(50000, 12.4, 60)
        self.assertRaises(ValueError)

    def test_calculate_interest_single_fee_case(self):
        Payment = PaymentCreditCard(90000, 2.4, 1)
        self.assertAlmostEqual(Payment.calculate_total_interest(), 0, places=2)

    def test_calculate_totala_interest_purchase_error(self):
        with self.assertRaises(ValueError):
            tarjeta_credito = PaymentCreditCard(0, 2.4, 60)

    def test_calculate_totala_interest_negative_error(self):
        with self.assertRaises(ValueError):
            tarjeta_credito = PaymentCreditCard(50000, 1, -10)

    # Casos de prueba para la responsabilidad R2: calcular_plan_amortizacion
    def test_calculate_amortization_plan(self):
        Payment = PaymentCreditCard(200000, 3.1, 36)
        plan = Payment.calculate_amortization_plan()
        self.assertEqual(len(plan), 36)
        self.assertAlmostEqual(plan[0][0], 9297.96, places=2)
        self.assertAlmostEqual(plan[-1][0], 9297.96, places=2)

    # Casos de prueba para la responsabilidad R3: calcular_efecto_pago_extra
    
    def test_calulate_amount_extra_effect_normal_case(self):
        Payment = PaymentCreditCard(200000, 3.1, 36)
        plan_with_extra = Payment.calculate_extra_payment(53000, 10)
        self.assertAlmostEqual(plan_with_extra[9][2], 43702.04, places=2)

    def test_calulate_amount_extra_effect_low_error(self):
        Payment = PaymentCreditCard(850000, 3.4, 24)
        with self.assertRaises(ValueError):
            plan_with_extra = Payment.calculate_extra_payment(45000, 10)

    def test_calulate_amount_extra_effect_late_error(self):
        Payment = PaymentCreditCard(850000, 3.4, 24)
        with self.assertRaises(ValueError):
            plan_with_extra = Payment.calculate_extra_payment(180000, 22)


if __name__ == "__main__":
    unittest.main()
