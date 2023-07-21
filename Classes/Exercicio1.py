class Pessoa:
    def __init__(self, _nome:str , _idade:int , _profissao = str("")) -> None:
        self.nome = _nome;
        self.idade = _idade;
        self.profissao = _profissao;

    def show(self):
        print(f'Nome: {self.nome}');
        print(f'Idade: {self.idade}');
        print(f'Profissão: {self.profissao}');

pessoa_1 = Pessoa("Bastião", 73, "Aposentado");
pessoa_2 = Pessoa("Enzo", 6, "Estudante");

pessoa_1.show();
print("\n");
pessoa_2.show();