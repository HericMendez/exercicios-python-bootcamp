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









