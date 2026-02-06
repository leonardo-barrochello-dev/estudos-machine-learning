class Conta:
    saldo : float
    titular : str
    
    def __init__(self, saldo : float, titular : str):
        self.saldo = saldo
        self.titular = titular

    def sacar(self, valor : float):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def depositar(self, valor:float):
        self.saldo += valor

class ContaCorrente(Conta):
    limite:float
    
    def __init__(self, saldo : float, titular : str, limite : float):
        super().__init__(saldo, titular)
        self.limite = limite
  
    def sacar(self, valor : float):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")
     

try:
    conta = ContaCorrente(100, "João", 100)
    conta.sacar(20000000000)
except ValueError as e:
    print(f"Operação negada : [{e}]")