A = int(0);
B = int(0);
C = int(0);
result = int(0);

print("O algoritmo verifica se a soma de A + B é menor ou maior que C.");

A = int(input("Digite o valor de A: "));
B = int(input("Digite o valor de B: "));
C = int(input("Digite o valor de C: "));

result = A + B;

if ( result > C ):
    print("A soma de A + B é MAIOR que C.");
    print(f'O valor de C é: {C} // A soma de A + B é: {result}');
else:
    if ( result < C):
        print("A soma de A + B é MENOR que C.");
        print(f'O valor de C é: {C} // A soma de A + B é: {result}');
    else:
        print("A soma de A + B é IGUAL a C.");