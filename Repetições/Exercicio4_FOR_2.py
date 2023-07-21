inputFatorial = int(0);
result = int(0);

print("O código a seguir calcula o fatorial do número digitado.");

inputFatorial = int(input("Digite um número positivo: "));
result = inputFatorial;

for count in range(inputFatorial - 1, 0, -1):
    result *= count;
    print(result);