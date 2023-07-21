from Exercicio1 import sumVectorIndexes;
from insertValues import insertVectorValues;

numbers = [];
sumNumbers = int(0);
result = float(0);

print("O algoritmo a seguir fará a soma dos elementos do vetor\nE exibirá a média aritmética.");

numbers = insertVectorValues();

sumNumbers = sumVectorIndexes(numbers);

result = sumNumbers / len(numbers);

print(f'O resultado é: {result}');