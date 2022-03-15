import random
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

round_winner = ""

pedra = """
###### Pedra ######
.    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
papel = """
###### Papel ######
.     ______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
tesoura = """
###### Tesoura ######
.    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
ascii_art = [pedra, papel, tesoura]

loop = "y"
while loop == "y":
    bot = random.randint(0,2)
    print("Faça sua jogada: ")
    
    player = int(input("""
    0 - Pedra 
    1 - Papel 
    2 - Tesoura
    >"""))
    
    #0: Pedra ; 1: Papel ; 2: Tesoura.
    print("")
    print("Sua jogada: ")
    print(ascii_art[player])
    print("Jogada do Bot:")
    print(ascii_art[bot])

    if player == bot :
        print("Empatou! \nMas como não existe meia vitória,\n vc perdeu! \n SEU NOIA SEU LIXO")

    else :
        if player == 0 :
            round_winner = "Player" if bot==2 else "Bot"
        if player == 1 :
            round_winner = "Player" if bot==0 else "Bot"
        if player == 2 :
            round_winner = "Player" if bot == 1 else "Bot"
        if player > 2 :
            "Opção inválida, seu burro!"

        print(round_winner, " venceu!")
    
    loop = input("Jogar novamente? (Y/N): ").lower()
    clearConsole()
    if not loop == "y" :
        print("game over")
        break
