from sumNumbers import sumNumbers;

def sumNumberOneToX():
    inputValue = int(0);
    result = int(0);

    print("O algoritmo a seguir fará a soma dos números de 1 a X.");

    inputValue = int(input("Digite um número: "));

    result = sumNumbers(inputValue);

    print(f'O resultado é: {result}');