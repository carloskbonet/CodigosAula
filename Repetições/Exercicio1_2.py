inputValue = (int);
inputStopCond = (int);

print("O algoritmo a seguir fará uma contagem crescente do número digitado.\n");

inputValue = int(input("Digite um número inteiro positivo : "));
inputStopCond = int(input("Digite um critério de parada: "));

while( inputValue <= inputStopCond ):
    print(inputValue);
    inputValue += 1;