class Conta:
    def __init__(self, titular: str, numero: int, saldo: int):
        self.t = titular
        self.n = numero
        self.s = saldo
    
    @property
    def deposito(self):
        v = int(input('digite o valor que deseja depositar na conta: '))
        self.s += v
        return f'depósito realizado com sucesso! seu saldo atual é de R$ {self.s:.2f}'


    @property
    def saque(self):
        v = int(input('insira o valor que deseja retirar na conta: '))
        if v > self.s:
            return f'o saque não pôde ser realizado pois o saldo atual da conta é de R$ {self.s:.2f}. para conseguir realizar o procedimento, informe um valor menor do que o saldo.'
        else:
            self.s -= v
            return f'saque realizado com sucesso! seu saldo atual é de R$ {self.s:.2f}'
            
c = Conta('faísca', 823475, 500)
print(c.deposito)
print(c.saque)
