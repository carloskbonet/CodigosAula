inputValue = (int);
checked = bool(False);
result = (str);

inputValue = int(input("Digite um número inteiro: "));

result = "Não solucionado";


if (inputValue > 0 and checked == False):
    checked = True;
    result = "O número digitado é positivo";
    
if (inputValue < 0 and checked == False):
    checked = True;
    result = "O número digitado é negativo";

if (inputValue == 0 and checked == False):
    checked = True;
    result = "O número digitado é 0";

print(result);