inputValue = (float);
inputTaxa = (float);
inputDays = (int);
valuePerDay = (float);
result = (float);

inputValue = float(input("Digite o valor da sua conta pendente: "));
inputTaxa= float(input("Digite a taxa cobrada diariamente\n(Entre 0 e 100): "));
inputDays = int(input("Digite o número de dias de atraso até o pagamento: "));

inputTaxa = inputTaxa / 100;

valuePerDay = inputValue * inputTaxa;

result = (valuePerDay * inputDays) + inputValue;

print(f'A taxa cobrada por dia é de {inputTaxa*100}%');
print(f'O valor inicial da conta é de : {inputValue} R$');
print(f'O valor cobrado diariamente em atrasos é de: {valuePerDay} R$');
print(f'O valor da conta após {inputDays} dias de atraso é de: {result} R$');