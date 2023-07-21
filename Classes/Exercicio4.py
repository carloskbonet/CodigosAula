class Animal:
    def __init__(self, _nome: str, _especie: str) -> None:
        animais = ["Gato", "Galo", "Grilo"];
        self.nome = _nome;
        if (_especie in animais):
            self.especie = _especie;
            if (_especie == "Galo"):
                self.sound = "Cocoricó";
            if (_especie == "Gato"):
                self.sound = "Miau";
            if (_especie == "Grilo"):
                self.sound = "Cricri";
        else:
            raise Exception("Especie not defined");

    def show(self):
        print(f'O animal é da espécie: {self.especie}');
        print(f'O nome do {self.especie} é {self.nome}');

    def emitirSom(self):
        if (self.especie == "Galo"):
            self.sound = "Cocoricó";
        if (self.especie == "Gato"):
            self.sound = "Miau";
        if (self.especie == "Grilo"):
            self.sound = "Cricri";
        print(f'O {self.especie} fez {self.sound}');
        

    def getNome(self):
        return self.nome;

    def setNome(self, _newName: str):
        self.nome = _newName;

    def getEspecie(self):
        return self.especie;

    def setEspecie(self, _newEspecie: str):
        self.especie = _newEspecie;