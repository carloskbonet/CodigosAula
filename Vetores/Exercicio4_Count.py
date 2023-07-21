from insertValues import insertVectorValues;

#A função verifica se um elemento está presente no vetor.
def verification(vector, element):
    for i in range(len(vector)):
        if ( vector[i] == element ):
            return True;

    return False;

numbers = [];
inputValue = int(0);
result = bool(False);

print("O algoritmo a seguir verifica se o número digitado está no vetor.");

numbers = insertVectorValues();

inputValue = int(input("Digite um valor para verificar se ele está no vetor: "));

result = verification(numbers, inputValue);

if (result == True):
    print("O valor está no vetor.");
else:
    print("O valor não está no vetor.");



#result = numbers.count(inputValue);
#if (result > 0):
#    print("O valor está no vetor.");
#else:
#    print("O valor não está no vetor.");