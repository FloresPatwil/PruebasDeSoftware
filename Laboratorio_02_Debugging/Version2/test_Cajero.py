
import unittest
from io import StringIO
from contextlib import redirect_stdout
from Cajero import Cajero


class TestCajero(unittest.TestCase):
    
    # test para verificar que el usuario exista
    def test_usuario(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["usuario"], "briyit")
        
    # test para verificar que la contraseña sea correcta
    def test_contrasena(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        self.assert_(cajero.usuarios["briyit"]["contrasena"] == 1234)
    # test para verificar que el monto sea correcto
    def test_monto(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        self.assert_(cajero.usuarios["briyit"]["monto"] == 5000)
    # test para verificar que el usuario no exista
    def test_usuario_no_existe(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertNotEqual(cajero.sesion["usuario"], "briyit2")
    # test para depositar
    def test_depositar(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 5000)
        cajero.depositar(1000)
        self.assertEqual(cajero.sesion["monto"], 6000)
    # test para depositar monto invalido
    def test_depositar_monto_invalido(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 5000)
        cajero.depositar(-1000)
        self.assertEqual(cajero.sesion["monto"], 5000)
    # test para depositar limite diario
    def test_depositar_limite_diario(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 5000)
        cajero.deposito_dia = 3000
        cajero.depositar(500)
        self.assertEqual(cajero.sesion["monto"], 5000)
    # test para retirar
    def test_retirar(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 5000)
        cajero.retirar(1000)
        self.assertEqual(cajero.sesion["monto"], 4000)
    # test para verificar que el monto sea suficiente para retirar
    def test_retirar_monto_insuficiente(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 500}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 500)
        cajero.retirar(1000)
        self.assertEqual(cajero.sesion["monto"], 500)
      
    def run_tests(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCajero)
        unittest.TextTestRunner().run(suite)
# creamos main para probar test
if __name__ == '__main__':
    TestCajero().run_tests()
    