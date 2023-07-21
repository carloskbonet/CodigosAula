from Exercicio5 import contaBancaria;
from classPessoa import Pessoa;

pessoa_1 = Pessoa("Alberto", 9991110123, "01/01/1970", "de Lima");
conta = contaBancaria(pessoa_1, 0);

while True:
    print("\nMenu de opções do banco.");
    print("Digite 0 para encerrar a consulta.");
    print("Digite 1 para visualizar o saldo atual da conta.");
    print("Digite 2 para depositar um valor na conta.");
    print("Digite 3 para sacar um valor na conta.\n");

    selectMenu = int(0);
    selectMenu = int(input("Digite: "));

    if (selectMenu < 0 or selectMenu > 3):
        print("Digite apenas opções presentes no menu.");
    else:
        if (selectMenu == 0):
            print("Passar bem.");
            exit();
        if (selectMenu == 1):
            conta.exibirSaldo();
        if (selectMenu == 2):
            valor = float(input("Digite o valor que deseja depositar: "));
            conta.depositar(valor);
        if (selectMenu == 3):
            valor = float(input("Digite o valor que deseja sacar: "));
            conta.sacar(valor);

