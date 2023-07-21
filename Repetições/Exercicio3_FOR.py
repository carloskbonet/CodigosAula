countStop = int(10);
result = int(0);

print("O codigo a seguir apresenta a soma dos números de 1 a X.");

print(f'Inicilizando result: {result}')

for count in range(1 , 11):
    result = result + (count);
    print (f'It: {count}  |  Result: {result}');

