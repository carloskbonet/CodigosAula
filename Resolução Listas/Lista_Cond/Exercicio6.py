inputSexo = str("");
inputAltura = float(0);
inputPeso = float(0);
result = float(0);

print("O algoritmo a seguir irá calcular o IMC do usuário.");

inputSexo = input("Digite F para feminino ou M para masculino: ");
inputAltura = float(input("Digite a sua altura: "));
inputPeso = float(input("Digite o seu peso: "));

result = inputPeso / (inputAltura * inputAltura);

result = round(result, 2);

if (inputSexo == "M"):
    if (result < 18.5):
        print(f'IMC {result}. Abaixo do peso.');
    if (result >= 18.5 and result <= 25):
        print(f'IMC {result}. Peso Normal.');
    if (result > 25 and result <= 30):
        print(f'IMC {result}. Acima do Peso.');
    if (result > 30):
        print(f'IMC {result}. Obeso.');
if (inputSexo == "F"):
    if (result < 17):
        print(f'IMC {result}. Abaixo do peso.');
    if (result >= 17 and result <= 23):
        print(f'IMC {result}. Peso Normal.');
    if (result > 23 and result <= 27):
        print(f'IMC {result}. Acima do Peso.');
    if (result > 27):
        print(f'IMC {result}. Obeso.');
