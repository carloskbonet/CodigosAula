from positiveNegativeZero_import import positiveNegativeOrZero;
from multiplication_import import tabuada;
from sumNumbers_import import sumNumberOneToX;

print("Algoritmo de seleção.");
print("A seguir está a lista de algoritmos a serem utilizados.");

inputChoice = int(0);

while (True):
    check = bool(False);

    print("\n");
    print("Digite o número correspondente :");
    print("# 0 para Encerrar o programa.");
    print("# 1 para (Algoritmo de Tabuada.)");
    print("# 2 para (Algoritmo para verificar se um número é positivo, negativo ou zero.)");
    print("# 3 para (Algoritmo para somar números de 1 a X.)");

    inputChoice = int(input("Digite: "));
    print("\n");

    if (inputChoice == 0):
        print("Programa encerrado.");
        exit();

    if (inputChoice == 1 and not check):
        tabuada();
        check = True;
    if (inputChoice == 2 and not check):
        positiveNegativeOrZero();
        check = True;
    if (inputChoice == 3 and not check):
        sumNumberOneToX();
        check = True;