#Função para transferir valores de um vetor para outro
def transfer(vector):
    vectorCopy = []
    aux = int(0);

    while True:
        aux = vector.pop();
        vectorCopy.insert(0, aux);
    
        if (len(vector) < 1):
            break;

    return vectorCopy;


numbers = [1,2,3,4,5,6];
numbersCopy = [];

print("O algoritmo a seguir irá transferir os números de um vetor para o outro.");

print(numbers);
print(numbersCopy);

numbersCopy = transfer(numbers);

print(numbers);
print(numbersCopy);