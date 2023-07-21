from classPessoa import Pessoa

class Livro:
    def __init__(self, _titulo: str, _autor: str, _editora: str, _anoPublicacao: int):
        self.titulo = _titulo;
        self.autor = _autor;
        self.editora = _editora;
        self.anoPublicacao = _anoPublicacao;
        self.disponivel = True;
        self.locador = None;

    def verificarDisponibilidade(self):
        #codigo para verificar se o livro está disponível.
        if (self.disponivel == True):
            print(f'O livro {self.titulo} está disponível.');
        else:
            print(f'O livro {self.titulo} NÃO está disponível. Atualmente locado por:');
            self.locador.exibirInformacoes();

    def emprestar(self, _locador: Pessoa):
        #codigo para emprestar o livro.
        if (self.disponivel == True):
            print(f'O livro {self.titulo} está disponível e será emprestado.');
            self.disponivel = False;
            self.locador = _locador;
        else:
            print(f'O livro {self.titulo} NÃO está disponível. Não é possível emprestar.');

    def devolver(self):
        #codigo para devolver o livro.
        if (self.disponivel == True):
            print(f'O livro {self.titulo} não está emprestado.');
        else:
            print(f'O livro {self.titulo} está emprestado e será devolvido.');
            self.disponivel = True;
            self.locador = None;

    def exibirInformacoes(self):
        print(self.titulo);
        print(self.autor);
        print(self.editora);
        print(self.anoPublicacao);
        print(self.disponivel);


livro_1 = Livro("Biblia Sagrada", "Jesus", "Belém", -2000);
livro_2 = Livro("Harry Potter", "JK Rolling", "Brasil", 2002);

pessoa_1 = Pessoa("João", "123.123.123", "01/01/2001", "Ferreira");
pessoa_2 = Pessoa("Marcelo", "321.321.321", "10/10/2010");

#livro_1.verificarDisponibilidade();
#livro_2.verificarDisponibilidade();


livro_2.emprestar(pessoa_1);

livro_2.verificarDisponibilidade();