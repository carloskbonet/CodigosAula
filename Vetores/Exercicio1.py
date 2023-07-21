#Soma os números do vetor
def sumVectorIndexes(vector):
    sumVector = float(0);

    for i in range(len(vector)):
        sumVector += vector[i];

    return sumVector;


def sumVectorAlgorithm():
    numbers = [];
    sumVector = float(0);

    print("O algoritmo a seguir fará a soma de todos os elementos do vetor.");

    print("Digite um número para ser inserido no vetor.\nDigite 0 para parar de inserir.");

    while True:
        inputValue = float(0);
        inputValue = float(input("Digite: "));

        if (inputValue != 0):
            numbers.append(inputValue);
        else:
            break;

    print("\nCalculando a soma dos elementos...\n");

    sumVector = sumVectorIndexes(numbers);

    print(f'O resultado da soma é: {sumVector}');