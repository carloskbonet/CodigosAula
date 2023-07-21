# Peso Total 10
inputNota1 = float(0);
inputNota2 = float(0);
inputNota3 = float(0);
result = float(0);

print("O algoritmo a seguir calcula a média ponderada das notas do aluno.");
print("A nota 1 tem peso 2.\nA nota 2 tem peso 3.\nA nota 3 tem peso 5.\n");

inputNota1 = float(input("Digite a primeira nota: "));
inputNota2 = float(input("Digite a segunda nota: "));
inputNota3 = float(input("Digite a terceira nota: "));

result = (inputNota1 * 2) + (inputNota2 * 3) + (inputNota3 * 5);
result = result / 10;

if (result < 0 or result > 10):
    print("As notas digitadas devem estar entre 0 e 10.");
else:
    print(f'\nA nota final do aluno é: {result}');

    if (result >= 7):
        print("O aluno foi APROVADO.");
    else:
        print("O aluno está REPROVADO.");