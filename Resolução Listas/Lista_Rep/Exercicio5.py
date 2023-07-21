inputAltura1 = float(0);
inputAltura2 = float(0);

inputCrescimento1 = float(0);
inputCrescimento2 = float(0);

print("O algoritmo calculará quantos anos a pessoa menor levará para superar a maior.");

inputAltura1 = float(input("Digite a altura da primeira pessoa: "));
inputAltura2 = float(input("Digite a altura da segunda pessoa: "));

inputCrescimento1 = float(input("Digite o crescimento anual da primeira pessoa: "));
inputCrescimento2 = float(input("Digite o crescimento anual da segunda pessoa: "));

#Repetição para calcular o crescimento das pessoas e verificar se ultrapassou o maior
for i in range(20):
    print(f'Altura atual do pessoa 1 : {round(inputAltura1,2)} no ano {i}');
    print(f'Altura atual do pessoa 2 : {round(inputAltura2,2)} no ano {i}');
    print("\n");

    if (inputAltura1 > inputAltura2):
        print(f'A pessoa menor superou o tamanho da maior em {i} anos.');
        print(f'A altura final da menor pessoa ficou em {round(inputAltura1,2)} e da maior em {round(inputAltura2,2)}');
        break;

    inputAltura1 += inputCrescimento1;
    inputAltura2 += inputCrescimento2;