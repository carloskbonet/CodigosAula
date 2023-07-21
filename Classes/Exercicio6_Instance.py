from Exercicio6 import Carro;
import random;


fiatUno = Carro("Uno");

while True:
    print("\nMenu de opções do carro.");
    print("Digite 0 para encerrar.");
    print("Digite 1 para ligar o carro.");
    print("Digite 2 para desligar o carro.");
    print("Digite 3 para Acelerar.");
    print("Digite 4 para Frear.\n");

    selectMenu = int(0);
    selectMenu = int(input("Digite: "));

    if (selectMenu < 0 or selectMenu > 4):
        print("Digite apenas opções presentes no menu.");
    else:
        if (selectMenu == 0):
            print("Programa encerrando.");
            exit();
        if (selectMenu == 1):
            fiatUno.ligar();        
        if (selectMenu == 2):
            fiatUno.desligar();
        if (selectMenu == 3):
            fiatUno.acelerar();
        if (selectMenu == 4):
            fiatUno.frear();