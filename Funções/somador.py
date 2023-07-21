from somador_import import somarDoisNumeros;

inputNumero = int(0);
resultado = int(0);
checked = bool(False);

print("O código a seguir é um somador. Digite um número para acumular com o resultado atual.");

while(checked == False):
    inputNumero = int(input("Digite um número: "));

    resultado = somarDoisNumeros(resultado, inputNumero);
    print(resultado);

    verification = input("\nVocê quer continuar? (y/n): ");
    if (verification == "n" or verification == "N"):
        checked = True;
        break;


# URI Programming