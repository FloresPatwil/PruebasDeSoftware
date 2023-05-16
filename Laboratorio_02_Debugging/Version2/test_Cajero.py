
import unittest
from io import StringIO
from contextlib import redirect_stdout
from Cajero import Cajero


class TestCajero(unittest.TestCase):
    
    """# test para verificar que el usuario exista
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
    # test para ver montos
    def test_ver_monto(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        self.assertEqual(cajero.sesion["monto"], 5000)
    # test para verificar que el monto sea correcto
    def test_monto_correcto(self):
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        self.assert_(cajero.usuarios["briyit"]["monto"] == 5000)
    # test para ver que el deposito sea correcto
    """
    def test_depositar_exito(self):
        print("-----------------test_depositar_exito")
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        cajero.depositar() # retiro 1000
        self.assertEqual(cajero.sesion["monto"], 6000)
        
    # test para ver el retiro fue exitoso
    def test_retirar_exito(self):
        print("test_retirar_exito")
        cajero = Cajero()
        cajero.usuarios = {"briyit": {"contrasena": 1234, "monto": 5000}}
        cajero.sesion = {"usuario": "", "monto": 0}
        cajero.sesion["usuario"] = "briyit"
        cajero.sesion["monto"] = cajero.usuarios[cajero.sesion["usuario"]]["monto"]
        cajero.retirar() # retiro 1000
        self.assertEqual(cajero.sesion["monto"], 4000)
    
    def run_tests(self):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCajero)
        unittest.TextTestRunner().run(suite)
# creamos main para probar test
if __name__ == '__main__':
    TestCajero().run_tests()
    