# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023

@author: LAB02 
"""
class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000.00
        self.retiro_dia = 0.00
        self.deposito_dia = 0.00
        self.menu()

    def contraseña(self):
        contador = 1
        while contador <= 3:
            x = int(input("ingrese su contraseña:" ))
            if x == 5467:
                print("Contraseña Correcta")
                break

            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador+=1
                
    def menu(self):
        self.contraseña()
        opcion = 0
        while opcion != "4":
            print(""" Bienvenido al cajero automatico

            ******Menú******

            1-  Depositar

            2- Retirar

            3- Ver saldo

            4- Salir """)

            opcion = input("Su opción es: ")

            if self.continuar:
                if opcion == "1" :
                    self.depositar()
                elif opcion == "2" :
                    self.retirar()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            else:

                if opcion in "123":
                    print("Imposible realizar esa operación")
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")

    def depositar(self):
        if self.deposito_dia >= 3000:
            print("Usted a alcanzado el límite de depósito diario.")
            return
        deposito = float(input("Ingrese su monto a depositar: "))
        if deposito <= 0:
            print("No puede depositar 0 o un monto negativo.")
            return
        elif deposito > 3000:
            print("No puede depositar más de s/3000 en un solo depósito.")
            return
        print("Usted ha depositado s/", deposito)
        # modificar el monto y limite de deposito diario
        self.monto += deposito
        self.deposito_dia += deposito
        print(f"Su nuevo saldo es s/{self.monto}")

    def retirar(self):
        if self.retiro_dia >= 3000:
            print("Ha alcanzado el límite de retiro diario.")
            return
        retiro=float(input("¿Cuánto desea retirar? : "))
        if retiro <= 0:
            print("Debe retirar almenos s/1.00")
            return
        elif retiro > 3000:
            print("No puede retirar más de s/3000 en un solo retiro.")
            return
        elif self.monto < retiro:
            print("Imposible realizar el retiro, su monto es menor.")
            return
        print("Su monto actual es s/", self.monto)
        self.monto-=retiro
        self.retiro_dia += retiro
        print(f"Usted a retirado: s/{retiro}", f"su nuevo monto es {self.monto}")

    def ver(self):
        print(f"Su saldo es: s/" , self.monto)

app = Cajero()