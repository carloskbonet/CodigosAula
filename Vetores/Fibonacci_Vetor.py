#Fibonacci

fibonacci = [0,1];
sumNumbers = int(0);
inputIndex = int(0);

print("O algoritmo a seguir calculará a sequência fibonacci.");

inputIndex = int(input("Digite a quantia de números a serem exibidos: "));

#for i in range(inputIndex-2):
#    sumNumbers = fibonacci[i] + fibonacci[i+1];
#    fibonacci.append(sumNumbers);

for i in range(2, inputIndex, 1):
    sumNumbers = fibonacci[i-1] + fibonacci[i-2];
    fibonacci.append(sumNumbers);

print("A seguir está a sequência fibonacci: ");

print(fibonacci);