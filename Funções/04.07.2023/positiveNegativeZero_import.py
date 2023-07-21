from positiveNegativeZero import isPositiveNegativeOrZero;

def positiveNegativeOrZero():
    inputValue = int(0);
    result = str("");

    print("O algoritmo a seguir verifica se o número digitado é:\n(Positivo, Negativo ou Zero).");

    inputValue = int(input("Digite um valor: "));

    result = isPositiveNegativeOrZero(inputValue);

    print(f'O resultado da função é: {result}');