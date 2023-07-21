class Pessoa:
    def __init__(self, _nome: str, _cpf: str, _nascimento: str, _sobrenome = str("")):
        self.nome = _nome;
        self.sobrenome = _sobrenome;
        self.cpf = _cpf;
        self.nascimento = _nascimento;

    def exibirInformacoes(self):
        print(f'Nome: {self.nome} {self.sobrenome}');
        print(f'CPF: {self.cpf}');
        print(f'Data de Nascimento: {self.nascimento}');