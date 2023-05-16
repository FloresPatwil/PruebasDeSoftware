class CajeroMejoradoPruebas:
    def __init__(self):
        self.monto = 5000.00
        self.retiro_dia = 0.00
        self.deposito_dia = 0.00

    def depositar(self, monto):
        if self.deposito_dia >= 3000:
            return False, "Usted a alcanzado el límite de depósito diario."
        if monto <= 0:
            return False, "No puede depositar 0 o un monto negativo."
        elif monto > 3000:
            return False, "No puede depositar más de s/3000 en un solo depósito."
        self.monto += monto
        self.deposito_dia += monto
        return True, f"Usted ha depositado s/{monto}. Su nuevo saldo es s/{self.monto}"

    def retirar(self, monto):
        if self.retiro_dia >= 3000:
            return False, "Ha alcanzado el límite de retiro diario."
        if monto <= 0:
            return False, "Debe retirar almenos s/1.00"
        elif monto > 3000:
            return False, "No puede retirar más de s/3000 en un solo retiro."
        elif self.monto < monto:
            return False, "Imposible realizar el retiro, su monto es menor."
        self.monto -= monto
        self.retiro_dia += monto
        return True, f"Usted ha retirado s/{monto}. Su nuevo saldo es s/{self.monto}"

    def ver(self):
        return self.monto

