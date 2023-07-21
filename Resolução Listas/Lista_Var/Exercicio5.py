inputYears = int(0);
days = int(0);
months = int(0);
hours = int(0);

print("O algoritmo a seguir irá converter o número digitado de anos para Dias, Meses e Horas.");

inputYears = int(input("Digite a sua idade: "));

days = inputYears * 365;
months = int(days / 30);
hours = days * 24;

print(f'Valores convertidos:')
print(f'{inputYears} anos');
print(f'{months} meses');
print(f'{days} dias');
print(f'{hours} horas');