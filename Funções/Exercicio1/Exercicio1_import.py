from Exercicio1 import calcularAreaRetangulo;
from checkType import convertToInt;

inputAltura = str("");
inputLargura = str("");
result = int(0);

print("O código a seguir calcula a área do retângulo");

inputAltura = input("Digite a Altura: ");
inputLargura = input("Digite a Largura: ");

inputAltura = convertToInt(inputAltura);
inputLargura = convertToInt(inputLargura);

if (inputAltura == 0 or inputLargura == 0):
    print("Digite apenas números.");
    exit();

result = calcularAreaRetangulo(inputAltura, inputLargura);

print(result);
