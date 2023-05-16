# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023

@author: LAB02 
"""
import os
import csv

class Cajero:

    def __init__(self):
        self.continuar = True
        self.deposito_dia = 0
        self.retiro_dia = 0
        self.usuarios = {} # Diccionario para guardar usuarios
        self.sesion = {"usuario": "", "monto": 0}
        self.readDatos()
        self.menu()


    def readDatos(self):
        # diccionario {'clave':valor,clave':valor}
        csvFile = open("./datos.csv","r")
        reader = csv.reader(csvFile)
        noReadFirst = True
        for row in reader:
            if(noReadFirst):
                noReadFirst = False
                continue
            key = row[0].lower() # nombre
            value = int(row[1]) # contrasena
            monto = int(row[2])
            self.usuarios[key] = {
                "contrasena": value,
                "monto": monto
            }
            
        
            

        # Considerar los casos en que el usuario se repite en el
        #  archivo de datos, e.x. "Briyit", "briYit", "bRiYIT"
        #  en dichos casos considerar el primer usuario
        #print(self.usuarios)
        

    def usuario(self):
        nombre = input("Ingrese su nombre de usuario: ").lower()
        listaUsuarios = list(self.usuarios.keys())
        
        if nombre in listaUsuarios:
            self.sesion["usuario"] = nombre
            self.sesion["monto"] = self.usuarios[self.sesion["usuario"]]["monto"]
            self.contrasena()
        else:
            print("Usuario inexistente. No puede realizar operaciones.")
            self.continuar = False

    def indexUsuario(self, nombre):
        idx = 0
        for x in self.usuarios:
            if(x["nombre"] == nombre): return idx
            idx += 1
        return -1
        
    def contrasena(self):
        pwUsuarioIngresado = self.usuarios[self.sesion["usuario"]]["contrasena"]
        print("Contraseña por verificar: ", pwUsuarioIngresado)
        contador = 1
        while contador <= 3:
            x = int(input("ingrese su contraseña:" )) # Validador de input tipo entero
            if pwUsuarioIngresado == x:
                print("Contraseña Correcta")
                break
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador+=1

    def menu(self):
        os.system("cls") # Esto es solo para windows
        self.usuario()
        opcion = 0
        while opcion != "4":
            #os.system("cls")
            print(""" Bienvenido al cajero automatico
            ******Menú******
            1- Depositar
            2- Retirar
            3- Ver saldo
            4- Salir """)
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1" :
                    self.depositar()
                elif opcion == "2" :
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    self.guardarDatos()
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
        if self.deposito_dia >= 3000: # Limite de deposito superado
            print("Usted a alcanzado el límite de depósito diario.")
            return
        deposito = float(input("Ingrese su monto a depositar: "))
        if deposito <= 0: # Deposito negativo
            print("No puede depositar 0 o un monto negativo.")
            return
        elif deposito > 3000:
            print("No puede depositar más de s/3000 en un solo depósito.")
            return
        print("Usted ha depositado s/", deposito)
        # modificar el monto y limite de deposito diario
        self.usuarios[self.sesion["usuario"]]["monto"] += deposito # Actualizar el diccionario
        self.sesion["monto"] += deposito # Actualizar la sesion
        self.deposito_dia += deposito
        print(f"Su nuevo saldo es {self.sesion['monto']}")

    def retiro(self):
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
        elif self.sesion["monto"] < retiro:
            print("Imposible realizar el retiro, su monto es menor.")
            return
        print("Su monto actual es: ", self.sesion["monto"])
        
        # modificar el monto y limite de retiro diario
        self.usuarios[self.sesion["usuario"]]["monto"] -= retiro
        self.sesion["monto"] -= retiro
        self.retiro_dia += retiro
        print(f"Usted a retirado s/{retiro} y su nuevo saldo es s/{self.sesion['monto']}")

    def ver(self):
        print("Su saldo", self.sesion["monto"])

    def guardarDatos(self):
        csvFile = open("./datos.csv","w")
        writer = csv.writer(csvFile)
        writer.writerow(["nombre","contrasena","monto"])
        for x in self.usuarios:
            writer.writerow([x,self.usuarios[x]["contrasena"],self.usuarios[x]["monto"]])
        csvFile.close()
        

        

app = Cajero()
