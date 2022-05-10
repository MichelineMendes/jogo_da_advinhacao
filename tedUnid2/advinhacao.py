import random
print("\n")
print("=" * 32)
print("Bem vindo ao jogo da advinhação")
print("=" * 32)
advinhar = """
          **
        *     *
       *       *
        *     *
             *
            *
            *
          
            *
"""
print(advinhar)
print("Nesse jogo você deve descobrir o número secreto, que pode ser qualquer número de 1 a 100")
jogar = 1

while jogar == 1:

    x = random.randint(1, 100)
    print(x) #esse print vai sair
    palpite = 0
    chances = 1

    print("\n\n**********  vamos começar!  **********")
    while palpite != x :
        palpite = int(input("\nQual o número secreto?   "))

        if palpite > x:
             print("Seu palpite foi muito alto")
             chances += 1
        elif palpite < x:
            print("Seu palpite foi muito baixo")
            chances += 1

    else:
        print("\n\nParabéns! Você descobriu o número secreto! Você usou ", chances, "tentativas")


    jogar = int(input("\nVocê deseja jogar novamente? Digite 1 para novo jogo ou qualquer outro caracter para sair:  "))

else:
    exit(0)
