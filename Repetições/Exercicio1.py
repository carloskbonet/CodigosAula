inputValue = (int);

print("O algoritmo a seguir fará uma contagem regressiva do número digitado.\n");

inputValue = int(input("Digite um número inteiro positivo : "));

while( inputValue >= 0 ):
    print(inputValue);
    inputValue -= 1;