inputFatorial = int(0);
result = int(1);

print("O código a seguir calcula o fatorial do número digitado.");

inputFatorial = int(input("Digite um número positivo: "));

for count in range(2, inputFatorial + 1, 1):
    result *= count;
    print(f'{result}');