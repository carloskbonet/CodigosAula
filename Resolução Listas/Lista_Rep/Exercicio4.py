inputQuantidadePessoas = int(0);
#possiveis votos
candidato1 = int(0);
candidato2 = int(0);
candidato3 = int(0);
candidato4 = int(0);
votoNulo = int(0);
votoBranco = int(0);

print("O algoritmo a seguir simulará uma votação.");

inputQuantidadePessoas = int(input("Digite quantas pessoas irão votar: "));

print("\nExistem candidatos referentes aos números de 1 a 4.");
print("Escolha 5 para voto Nulo ou 6 para voto em Branco.\n");

for i in range(1, inputQuantidadePessoas + 1):
    voto = int(0);
    while True:
        voto = int(input(f'Pessoa {i}, digite o seu voto: '));
        
        if (voto <= 0 or voto >= 7):
            print("Digite apenas números válidos na votação.");
        else:
            if (voto == 1):
                candidato1 += 1;
            if (voto == 2):
                candidato2 += 1;
            if (voto == 3):
                candidato3 += 1;
            if (voto == 4):
                candidato4 += 1;
            if (voto == 5):
                votoNulo += 1;
            if (voto == 6):
                votoBranco += 1;
            break;


print("\nQuantidade de votos coletados:");
print(f'Candidato 1: {candidato1}');
print(f'Candidato 2: {candidato2}');
print(f'Candidato 3: {candidato3}');
print(f'Candidato 4: {candidato4}');
print(f'Votos Nulos: {votoNulo}');
print(f'Votos em Branco: {votoBranco}');