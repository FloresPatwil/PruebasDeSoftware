import unittest
from CajeroMejoradoPruebas import CajeroMejoradoPruebas
class TestCajero(unittest.TestCase):
    def setUp(self):
        self.cajero = CajeroMejoradoPruebas()

    def test_depositar_exito(self):
        result, message = self.cajero.depositar(1000)
        self.assertTrue(result)  # Si hay resultado
        self.assertEqual(message, "Usted ha depositado s/1000. Su nuevo saldo es s/6000.0")
        self.assertEqual(self.cajero.ver(), 6000.00)

    def test_depositar_limite_diario(self):
        self.cajero.deposito_dia = 3000
        result, message = self.cajero.depositar(500)
        self.assertFalse(result)  # No hay resultado
        self.assertEqual(message, "Usted a alcanzado el límite de depósito diario.")
        self.assertEqual(self.cajero.ver(), 5000.00)

    def test_depositar_monto_invalido(self):
        result, message = self.cajero.depositar(-8000)
        self.assertFalse(result)  # No hay resultado
        self.assertEqual(message, "No puede depositar 0 o un monto negativo.")
    


