#Encontra o maior valor do vetor

numbers = [];
bNumber = int(0);
lNumber = int(0);

print("O algoritmo a seguir mostrará o maior valor do vetor.");
print("Digite números para serem inseridos no vetor.\nDigite 0 para parar de inserir.");

while True:
    inputValue = int(0);
    inputValue = int(input("Digite: "));

    if (inputValue == 0):
        break;
    else:
        numbers.append(inputValue);

if (numbers[0]):
    bNumber = numbers[0];
    lNumber = numbers[0];

for i in range(len(numbers)):
    if( numbers[i] > bNumber ):
        bNumber = numbers[i];
    if( numbers[i] < lNumber ):
        lNumber = numbers[i];

print(f'O maior valor encontrado no vetor foi: {bNumber}');
print(f'O menor valor encontrado no vetor foi: {lNumber}');