def contaAteONumero(numero1: int, numero2: int):
    if (numero1 <= numero2):
        print(numero1);
        return contaAteONumero(numero1 + 1, numero2);



contaAteONumero(1,10);