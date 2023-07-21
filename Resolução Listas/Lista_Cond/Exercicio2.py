A = int(0);
B = int(0);
C = int(0);
checked = False;

print("O algoritmo irá exibir os valores digitados em ordem decrescente.");

A = int(input("Digite um valor: "));
B = int(input("Digite um valor: "));
C = int(input("Digite um valor: "));

if (A >= B and A >= C and checked == False):
    checked = True;
    print(A);
    if (B >= C):
        print(B);
        print(C);
    else:
        print(C);
        print(B);

if (B >= A and B >= C and not checked):
    checked = True;
    print(B);
    if( A >= C ):
        print(A);
        print(C);
    else:
        print(C);
        print(A);

if (C >= A and C >= B and not checked):
    checked = True;
    print(C);
    if (A >= B):
        print(A);
        print(B);
    else:
        print(B);
        print(A);
