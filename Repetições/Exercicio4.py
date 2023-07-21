count = int(0);
inputFatorial = int(0);

print("O código a seguir calcula o fatorial do número digitado.");

inputFatorial = int(input("Digite um número positivo: "));
count = inputFatorial - 1;

while(count > 0):
    print(f'{inputFatorial} x {count} :');
    inputFatorial *= count;
    print(f'Resultado: {inputFatorial}');
    count -= 1;