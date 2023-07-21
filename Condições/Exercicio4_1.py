inputYear = (int);
result = (int);
lastYear = (int);
nextYear = (int);
checked = bool(False);

print("O algoritmo a seguir irá verificar se o ano digitado é bissexto");
print("Digite Sair para encerrar o algoritmo.");

while(checked == False):
    inputYear = input("Digite um ano: ");

    if (inputYear == "Sair" or inputYear == "sair"):
        print("O programa encerrou.");
        exit();

    if (inputYear.isdigit()):
        inputYear = int(inputYear);
        checked = True;
    else:
        print("Digite apenas números inteiros.");

result = inputYear % 4;

if (result == 0):
    lastYear = inputYear - 4;
    nextYear = inputYear + 4;
    print("O ano digitado é bissexto.");
    print(f'O ano digitado foi {inputYear}');
    print(f'O ano bissexto anterior foi {lastYear}');
    print(f'O próximo ano bissexto será {nextYear}');
else:
    print("O ano digitado NÃO é bissexto.");