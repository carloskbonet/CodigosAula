from classPessoa import Pessoa;
import random;

class contaBancaria:
    def __init__(self, _titular: Pessoa, _saldoInicial: float) -> None:
        self.titular = _titular;
        self.numero = random.randint(1000,10000);
        self.saldo = _saldoInicial;

    def depositar(self, value: float):
        if (value > 0):
            self.saldo += value;
            print("Valor depositado com sucesso.");
            print(f'Novo saldo da conta: R$ {self.saldo}');
            return True;
        else:
            print("Não é possível depositar este valor.");
            return False;

    def sacar(self, value: float):
        if (value <= self.saldo):
            self.saldo -= value;
            print("Valor sacado com sucesso.");
            print(f'Novo saldo da conta: R$ {self.saldo}');
            return True;
        else:
            print("Não é possível sacar este valor. Saldo insuficiente.");
            return False;

    def exibirSaldo(self):
        print(f'O saldo atual da conta é: R$ {self.saldo}');
        return self.saldo;

    def getTitular(self):
        return self.titular;

    def setTitular(self, _newTitular: Pessoa):
        self.titular = _newTitular;

    def getNumero(self):
        return self.numero;

    def setNumero(self, _newNumero: int):
        self.numero = _newNumero;

    def getSaldo(self):
        return self.saldo;

    def setSaldo(self, _newSaldo: float):
        self.saldo = _newSaldo;
