inputLargura = (float);
inputAltura = (float);
resultado = (float);

inputLargura = float(input("Digite a largura do retângulo: "));
inputAltura = float(input("Digite a altura do retângulo: "));

resultado = inputLargura * inputAltura;

print(f'A altura do retângulo é: {inputAltura}\n'+
      f'e a largura do retângulo é: {inputLargura}')

print(f'O resultado abaixo é o cálculo da área do retângulo\n{resultado}');