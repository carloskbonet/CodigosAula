#Algoritmo para verificar se o vetor está ordenado de forma crescente.
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

numbers = [];
isOrdenado = True;

numbers = insertVectorValues();

for i in range(0, len(numbers) - 1, 1):
    #verificar se está desordenado.
    #se não estiver ordenado
    if( numbers[i] > numbers[i+1] ):
        isOrdenado = False;
        break;
    
print(f'\n{numbers}\n');

if (isOrdenado == True):
    print("O vetor está ordenado.");
else:
    print("O vetor NÃO está ordenado.");