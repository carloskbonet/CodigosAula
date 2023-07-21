inputCelsius = (float);
resultFahrenheit = (float);

inputCelsius = float(input("Digite a temperatura em Celsius: "));

resultFahrenheit = inputCelsius * 1.8;
resultFahrenheit = resultFahrenheit + 32;

print(f'O resultado a seguir é a conversão da temperatura de ° Celsius para Fahrenheit');

print(round(resultFahrenheit, 2));