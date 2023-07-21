#Código para o jogo de adivinhação
import random;
import time;

#Menu Vars
selectDif = int(0);
selectMenuGameplay = int(0);
#Gameplay vars
sortedNumber = int(0);
tryNumber = int(0);
tipNumber = int(0)
#Life Vars
tips = int(5);
tries = int(4);

print("Esse é o jogo da adivinhação !!");
print("Para jogar, temos algumas regras.");
print("Primeiro: Um número aleatório será gerado a partir da dificuldade selecionada.");
print("Segundo: O jogador receberá até 5 dicas.");
print("Terceiro: O jogador terá 4 tentativas.\n");


while True:
    print("Agora vamos começar pela seleção da dificuldade !");
    print("O modo fácil apresenta números entre 1 e 30");
    print("O modo medio apresenta números entre 1 e 60");
    print("O modo difícil apresenta números entre 1 e 90");
    print("Digite 1 para fácil\nDigite 2 para medio\nDigite 3 para difícil\n");

    selectDif = int(input("Digite: "));

    if (selectDif < 1 or selectDif > 3):
        print("\nDigite apenas números presentes no menu !!\n");
    else:
        sortedNumber = random.randint(1, selectDif * 30);
        break;

print(sortedNumber);

while True:
    print(f'Número de tentativas restantes: {tries} / Número de dicas restantes: {tips}');
    print("Menu do jogo. Selecione uma das opções abaixo.");
    print("Digite 1 para receber uma dica");
    print("Digite 2 para tentar adivinhar o número");
    print("Digite 3 para desistir do jogo");

    selectMenuGameplay = int(input("Digite: "));

    if (selectMenuGameplay < 1 or selectMenuGameplay > 3):
        print("\nDigite apenas números presentes no menu !!\n");
    else:
        if (selectMenuGameplay == 1 and tips > 0):
            tips -= 1;
            print("\nAaaah, então você quer uma dica, é? Bem... deixe me pensar um pouco.");
            time.sleep(1);
            print("Digite um número e vou te dizer se ele tá perto ou longe do meu número.");
            tipNumber = int(input("Digite: "));

            if (tipNumber == sortedNumber):
                print("Hmm... desisti da ideia, você não merece uma dica.");
            else:
                if (tipNumber >= (sortedNumber - 5) and tipNumber <= (sortedNumber + 5)):
                    print("Tá quente... MUITO quente. Você está quase lá !!\n");
                else:
                    if (tipNumber >= (sortedNumber - 10) and tipNumber <= (sortedNumber + 10)):
                        print("Tá quente... Mas nem tanto. Eu confio que você consegue.\n");
                    else:
                        print("Ish. Tu tá longe demais amigo, tenta com outro número.\n");


        if (selectMenuGameplay == 2):
            print("\nCorajoso!! Vai tentar adivinhar o número então, é? Hehe Boa sorte.");
            tryNumber = int(input("Digite: "));

            if (sortedNumber == tryNumber):
                print("Uau, não estava esperando por isso!! Haha você realmente acertou!!!!! Meus parabéns");
                exit();
            else:
                print("Buuuuuuh não foi dessa vez !!!\n");
                tries -= 1;

            if (tries < 1):
                print("Game Over.");
                exit();

        if (selectMenuGameplay == 3):
            print("\nUma pena !! Acreditei que você não era tão medroso...");
            exit();