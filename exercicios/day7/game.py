import random

import dados



vidas = 6
ascii = 0
fruits = ["orange", "banana", "apple", "grape"]
chosen_word = []



word_rng = random.choice(dados.words)
print(f"word is: {word_rng}")

for n in range(len(word_rng)):
    chosen_word+="_"

game_over = False
display = f"""
{dados.hominho_forca[0]} {''.join(chosen_word)}

"""
print(display)
print(vidas)

print(chosen_word)

while not game_over:
    print(display)
    user_input = input("solta a letra maluco:")
    print(display)

    for n in range(len(word_rng)):
        letter = word_rng[n]

        display += " "
        #print("Right") if word_rng[n] == user_input else print("Wrong")
        if word_rng[n] == user_input:
            chosen_word[n] = letter
        
    

        
    
    if user_input not in chosen_word :
        vidas+-1
        ascii+=1

        if vidas==0:
            game_over ==True
            print(display)
            print(chosen_word)
            print("Game Over!")
            break

    if "_" not in chosen_word :
        game_over = True
        print(display)
        print("You win!")

        break
    
    
    
    display = f"""
    {dados.hominho_forca[ascii]} {' '.join(chosen_word)}

    """






    
        
    