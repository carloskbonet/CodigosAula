PASSWORD = "A-very-very-long-password";
inputPassword = str("");

print("O algoritmo a seguir irá verificar se a senha digitada está de acordo com a senha armazenada no código.");

inputPassword = input("Digite a senha: ");

if(inputPassword == PASSWORD):
    print("Status: 200. Logged In.");
else:
    print("Status: 403. Not Authorized.");