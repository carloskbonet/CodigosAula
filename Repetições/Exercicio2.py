inputValue = (int);
result = (int);
count = int(1);
countStop = (int);

print("O código a seguir mostrará a tabuada do número digitado.");

inputValue = int(input("Digite um número: "));
countStop = int(input("Digite até qual valor o número deve ser multiplicado: "));

while(count <= countStop):
    result = inputValue * count;
    print(f'{inputValue} x {count} = {result}');
    count += 1;

#for count in range(1, countStop + 1, 1):
#    result = inputValue * count;
#    print(f'{inputValue} x {count} = {result}');
 
 
