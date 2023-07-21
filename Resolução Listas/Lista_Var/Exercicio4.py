inputValue1 = int(0);
inputValue2 = int(0);
aux = int(0);

print("O algoritmo a seguir irá inverter os valores das variáveis.");

inputValue1 = int(input("Digite o primeiro valor: "));
inputValue2 = int(input("Digite o segundo valor: "));

print(f'Antes\nVar 1: {inputValue1}  //  Var 2: {inputValue2}');

aux = inputValue1;
inputValue1 = inputValue2;
inputValue2 = aux;

print(f'Depois\nVar 1: {inputValue1}  //  Var 2: {inputValue2}');