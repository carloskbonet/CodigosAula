from multiplication import multiplication;

def tabuada():
    inputValue = int(0);
    result = int(0);
    count = int(1);
    countStop = int(10);

    print("O algoritmo a seguir apresentará a tabuada do número digitado.");

    inputValue = int(input("Digite um número: "));

    while(count <= countStop):
        result = multiplication(inputValue, count);
        print(f'{inputValue} X {count} = {result}');

        count += 1; 