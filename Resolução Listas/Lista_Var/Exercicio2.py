inputFahrenheit = float(0);
result = float(0);

print("O algoritmo a seguir irá converter a temperatura digitada em Fahrenheit para Celsius.");

inputFahrenheit = int(input("Digite uma temperatura: "));

result = (inputFahrenheit - 32) / 1.8;

print(f'A temperatura convertida para Celsius é: {result}');