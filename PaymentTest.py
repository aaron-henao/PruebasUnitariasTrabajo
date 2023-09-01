import unittest
from Payment import PaymentCreditCard


class TestDeudaTarjetaCredito(unittest.TestCase):

    # Casos de prueba para la responsabilidad R1: calcular_intereses_totales
    def test_calculo_intereses_totales_caso_normal(self):
        tarjeta_credito = PaymentCreditCard(200000, 3.1, 36)
        self.assertAlmostEqual(tarjeta_credito.calculate_total_interest(), 134726.53, places=2)

    def test_calculo_intereses_totales_caso_normal_2(self):
        tarjeta_credito = PaymentCreditCard(850000, 3.4, 24)
        self.assertAlmostEqual(tarjeta_credito.calculate_total_interest(), 407059.97, places=2)

    def test_calculo_intereses_totales_tasa_cero(self):
        tarjeta_credito = PaymentCreditCard(480000, 0, 48)
        self.assertAlmostEqual(tarjeta_credito.calculate_total_interest(), 0, places=2)

    def test_calculo_intereses_totales_usura(self):
        tarjeta_credito = PaymentCreditCard(50000, 12.4, 60)
        self.assertRaises(ValueError)

    def test_calculo_intereses_totales_cuota_unica(self):
        tarjeta_credito = PaymentCreditCard(90000, 2.4, 1)
        self.assertAlmostEqual(tarjeta_credito.calculate_total_interest(), 0, places=2)

    def test_calculo_intereses_totales_error_compra(self):
        with self.assertRaises(ValueError):
            tarjeta_credito = PaymentCreditCard(0, 2.4, 60)

    def test_calculo_intereses_totales_error_negativo(self):
        with self.assertRaises(ValueError):
            tarjeta_credito = PaymentCreditCard(50000, 1, -10)

    # Casos de prueba para la responsabilidad R2: calcular_plan_amortizacion
    def test_calcular_plan_amortizacion(self):
        tarjeta_credito = PaymentCreditCard(200000, 3.1, 36)
        plan = tarjeta_credito.calculate_amortization_plan()
        self.assertEqual(len(plan), 36)
        self.assertAlmostEqual(plan[0][0], 9297.96, places=2)
        self.assertAlmostEqual(plan[-1][0], 9297.96, places=2)

    # Casos de prueba para la responsabilidad R3: calcular_efecto_pago_extra
    
    def test_calcular_efecto_abono_extra_caso_normal(self):
        tarjeta_credito = PaymentCreditCard(200000, 3.1, 36)
        plan_con_abono = tarjeta_credito.calculate_extra_payment(53000, 10)
        self.assertAlmostEqual(plan_con_abono[9][2], 43702.04, places=2)

    def test_calcular_efecto_abono_extra_error_bajo(self):
        tarjeta_credito = PaymentCreditCard(850000, 3.4, 24)
        with self.assertRaises(ValueError):
            plan_con_abono = tarjeta_credito.calculate_extra_payment(45000, 10)

    def test_calcular_efecto_abono_extra_error_tardio(self):
        tarjeta_credito = PaymentCreditCard(850000, 3.4, 24)
        with self.assertRaises(ValueError):
            plan_con_abono = tarjeta_credito.calculate_extra_payment(180000, 22)


if __name__ == "__main__":
    unittest.main()
