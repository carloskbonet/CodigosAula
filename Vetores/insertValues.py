#Essa função insere os valores em um vetor e retorna o vetor cheio.
def insertVectorValues():
    vector = [];

    while True:
        inputValue = float(0);
        inputValue = float(input("Digite: "));

        if (inputValue != 0):
            vector.append(inputValue);
        else:
            break;

    return vector;