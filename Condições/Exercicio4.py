inputYear = (int);
result = (int);

print("O algoritmo a seguir irá verificar se o ano digitado é bissexto");
inputYear = int(input("Digite um ano: "));

result = inputYear % 4;

if (result == 0):
    print("O ano digitado é bissexto.");
    print(f'O ano digitado foi {inputYear}');
    print(f'O ano bissexto anterior foi {inputYear - 4}');
    print(f'O próximo ano bissexto será {inputYear + 4}');
else:
    print("O ano digitado NÃO é bissexto.");