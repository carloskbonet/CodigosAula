inputNome = str("");
inputSexo = str("");
inputEstadoCivil = str("");
inputAnosCasado = int(0);

print("O algoritmo a seguir vai registrar algumas informações do usuário.");

inputNome = input("Digite o seu nome: ");
inputSexo = input("Digite F para feminino ou M para masculino: ");
inputEstadoCivil = input("Digite Casado / Casada / Solteiro / Solteira: ");
 
print("\n");

if (inputEstadoCivil == "Casado" or inputEstadoCivil == "Casada"):
    inputAnosCasado = int(input(f'Digite a quantos anos está {inputEstadoCivil}: '));
    print("\n");
    print(f'Anos de casamento: {inputAnosCasado}');

print(f'Nome: {inputNome}');
print(f'Sexo: {inputSexo}');
print(f'Estado Civil: {inputEstadoCivil}');

