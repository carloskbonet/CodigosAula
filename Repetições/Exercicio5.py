numeroInicial = int(1);
segundoNumero = int(2);
proximoNumero = int(0);

print(numeroInicial);
print(segundoNumero);

for x in range(30):
    proximoNumero = numeroInicial + segundoNumero;

    numeroInicial = segundoNumero;
    segundoNumero = proximoNumero;

    print(proximoNumero);
