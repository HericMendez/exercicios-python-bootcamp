
#Random cara ou coroa
import random

moeda = random.choice(["Cara", "Coroa"])

print(moeda)

####################################################################################

#Roleta Russa:
import random

bullets = [1,0,0,0,0,0]

random.shuffle(bullets)

print("Welcome to the Russian Roulette!")
print("")
start = input("Pull the Trigger? (Y/N): ")
print("")
#print(bullets)


while start == "y" or start=="Y" :
    if(bullets[0] == 1) :
        print("")
        print("Congrats, you're dead!")
        print("")
        
        break
        
    else:
        
        print("")
        print("You pull the trigger.")
        print(". . .")
        print("*CLICK* Nothing happens.")
        print("")
        
        shot = bullets.pop(0)
        giveup = input("Give up? (Y/N): ")
        print("")
        
        
        if giveup == "y" or giveup == "Y" :
            print("You gave up!")
            break


####################################################################################


#Random Nuclear Throne Mutations:
import random;

mutations_string = "Gamma Guts, Second Stomach, Strong Spirit, Bolt Marrow, Boiling Vens, Throne Butt, Rhino Skin, Laser Brain, Recycle Gland, Shotgun Shoulders, Lucky Shot, Heavy Heart, Bloodlust, Back Muscle, Eagle Eyes, Euphoria, Last Wish, Extra Feet, Hammerhead, Impact Wrists, Long Arms, Open Mind, Patience, Plutonium Hunger, Rabbit Paw, Scarier Face, Trigger Fingers"

mutations = []
mutations = mutations_string.split(", ")

#this is one way to get a random result from a list:
#random.shuffle(mutations)
#print(mutations[0])

#and this does the same, but written differently:
index = random.randint(0, len(mutations)-1)
print(mutations[index])

# the first way shuffles the list and returns the element at index zero,
# while in the second one, it returns the element in a random index, 
# without altering the original list.

####################################################################################

import emoji
 
import random

emojis = [["⬜", "💩"], ["⬜","👿"], ["⬜","💀"], ["⬜","👽"], ["⬜","🤢"], ["⬜","🤣"], ["⬜","😍"], ["⬜","🙈"]]

emojis.extend(emojis)
#random.shuffle(emojis)



first_row = emojis[0:4] 
second_row = emojis[4:8] 
third_row = emojis[8:12] 
fourth_row = emojis[12:16] 


grid = [first_row, second_row, third_row, fourth_row]

hidden = True
n = 0
if(hidden ==False):
    n = 1

print(f"{grid[0][0][n]}  {grid[0][1][n]}  {grid[0][2][n]}  {grid[0][3][n]} ") 
print(f"{grid[1][0][n]}  {grid[1][1][n]}  {grid[1][2][n]}  {grid[1][3][n]} ") 
print(f"{grid[2][0][n]}  {grid[2][1][n]}  {grid[2][2][n]}  {grid[2][3][n]} ") 
print(f"{grid[3][0][n]}  {grid[3][1][n]}  {grid[3][2][n]}  {grid[3][3][n]} ") 




if(emojis[0] == emojis[8]):
    print("equal")
else:
    print("not equal")
























