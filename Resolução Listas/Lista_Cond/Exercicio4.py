inputBirthYear = int(0);
inputYear = int(0);
yearsOld = int(0);
yearsLeft = int(0);

print("O algoritmo a seguir irá verificar se a pessoa poderá votar na próxima eleição.");

inputBirthYear = int(input("Digite o ano do seu nascimento: "));
inputYear = int(input("Digite o ano atual: "));

#Calcula a idade da pessoa
yearsOld = inputYear - inputBirthYear;

if ((inputYear % 5) == 0):
    print(f'O ano atual {inputYear} é um ano de eleição.');
    print(f'A idade da pessoa nascida no ano {inputBirthYear} é {yearsOld} anos.');

    if (yearsOld >= 16):
        print(f'Ela está apta a votar nessa eleição.');
    else:
        print(f'Ela NÃO está apta a votar nessa eleição.');
else:
    print(f'O ano atual não é um ano de eleição.');
    yearsLeft = 5 - (inputYear % 5)
    print(f'O próximo ano de eleição será em: {inputYear + yearsLeft}');
    print(f'A pessoa terá {yearsOld + yearsLeft} anos na próxima eleição.');
    if (yearsOld + yearsLeft >= 16):
        print(f'Ela está apta a votar na próxima eleição.');
    else:
        print(f'Ela NÃO está apta a votar na próxima eleição.');
    

