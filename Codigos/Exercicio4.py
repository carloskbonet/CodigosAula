inputProductValue = (float);
inputProductDesc = (int);
result = (float);
result2 = (float);

inputProductValue = float(input("Digite o valor do produto: "));
inputProductDesc = int(input("Digite o valor do desconto: "));

result = inputProductValue * (inputProductDesc/100);
result2 = inputProductValue - result;

print(f'O valor a seguir é o desconto em reais obtido na compra:'
      f'{round(result, 2)}')
print(f'O valor a seguir é o preço do produto com o desconto:'
      f'{round(result2, 2)}')