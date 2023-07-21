#Notas
inputNotaAluno1 = (float);
inputNotaAluno2 = (float);
#Const
nota_alvo = float(7.0);
#Resultado
resultCalc = (float);

print("Esse é um algoritmo que calcula as notas semestrais dos alunos.\n");

inputNotaAluno1 = float(input("Digite a nota do aluno no primeiro semestre: "));
inputNotaAluno2 = float(input("Digite a nota do aluno no segundo semestre: "));

resultCalc = (inputNotaAluno1 + inputNotaAluno2) / 2;

print(f'A nota do aluno na matéria X é: {resultCalc}');

if (resultCalc >= nota_alvo):
    print("O aluno está aprovado");
else:
    print("O aluno está reprovado");    