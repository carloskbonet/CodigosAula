count = int(1);
countStop = int(10);
result = int(0);

print("O codigo a seguir apresenta a soma dos números de 1 a X.");

countStop = int(input("Digite um número: "));

while( count <= countStop ):
    result += count;
    print(result);

    count += 1;