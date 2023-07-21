class Carro:
    def __init__(self, _modelo: str) -> None:
        carros = ["Uno", "Palio", "Bugatti Veyron"];
        self.velocidadeAtual = 0;
        self.ligado = False;

        if (_modelo in carros):
            if (_modelo == "Uno"):
                self.modelo = "Uno";
                self.marca = "Fiat";
                self.ano = 2007;
                self.velocidadeMaxima = 160;
                self.aceleracao = 8;
            if (_modelo == "Palio"):
                self.modelo = "Palio";
                self.marca = "Fiat";
                self.ano = 2010;
                self.velocidadeMaxima = 180;
                self.aceleracao = 10;
            if (_modelo == "Bugatti Veyron"):
                self.modelo = "Bugatti Veyron";
                self.marca = "Bugatti";
                self.ano = 2018;
                self.velocidadeMaxima = 400;
                self.aceleracao = 40;
        else:
            raise Exception("Car not found");

    def ligar(self):
        if (self.ligado == False):
            self.ligado = True;
            print("O carro foi ligado com sucesso.");
        else:
            print("O carro já está ligado.");

    def desligar(self):
        if (self.ligado == True):
            if (self.velocidadeAtual == 0):
                self.ligado = False;
                print("O carro foi desligado com sucesso.");
            else:
                print("Não é possível desligar. O carro está em movimento.");
        else:
            print("O carro já está desligado.");
    
    def acelerar(self):
        if (self.ligado == True):
            if ((self.velocidadeAtual + self.aceleracao) <= self.velocidadeMaxima):
                self.velocidadeAtual += self.aceleracao;
                print(f'O carro está acelerando. Atualmente em: {self.velocidadeAtual} Km/H');
            else:
                self.velocidadeAtual = self.velocidadeMaxima;
                print(f'O carro está mantendo a velocidade atual de {self.velocidadeAtual} Km/H');
        else:
            print("O carro não está ligado.");

    def frear(self):
        if (self.ligado == True):
            if ((self.velocidadeAtual - self.aceleracao) >= 0):
                self.velocidadeAtual -= self.aceleracao;
                print(f'O carro está freando. Atualmente em: {self.velocidadeAtual} Km/H');
            else:
                self.velocidadeAtual = 0;
                print(f'O carro está parado.');
        else:
            print("O carro não está ligado.");

    def exibirInformacoes(self):
        print(f'Modelo: {self.modelo}');
        print(f'Marca: {self.marca}');
        print(f'Ano: {self.ano}');
        print(f'Velocidade Máxima: {self.velocidadeMaxima}');
        print(f'Aceleração: {self.aceleracao}');