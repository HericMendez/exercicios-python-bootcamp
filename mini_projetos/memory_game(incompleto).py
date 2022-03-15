import random
import os
clear = lambda: os.system('cls')

emojis = ['🤢', '🤣', '👽', '🤣', 
          '💩', '😍', '😍', '👿', 
          '💀', '🤢', '💩', '👽', 
          '👿', '🙈', '🙈', '💀']

hidden_grid = [['⬜', '⬜', '⬜', '⬜'], 
               ['⬜', '⬜', '⬜', '⬜'],
               ['⬜', '⬜', '⬜', '⬜'], 
               ['⬜', '⬜', '⬜', '⬜']]





#random.shuffle(emojis)

print("")
first_row = emojis[0:4]
second_row = emojis[4:8]
third_row = emojis[8:12]
fourth_row = emojis[12:16]


emoji_grid = [first_row, second_row, third_row, fourth_row]


def memory_game(emoji1, emoji2):
    score = 0


    
    emoji1_pos = emoji1.split(",")
    e1x = int(emoji1_pos[0])
    e1y = int(emoji1_pos[1])
  
    emoji2_pos = emoji2.split(",")
    e2x = int(emoji2_pos[0])
    e2y = int(emoji2_pos[1])




    print("    0    1     2    3")

    print(f"0  {emoji_grid[0][0]}   {emoji_grid[0][1]}   {emoji_grid[0][2]}   {emoji_grid[0][3]}") 
    print(f"1  {emoji_grid[1][0]}   {emoji_grid[1][1]}   {emoji_grid[1][2]}   {emoji_grid[1][3]}") 
    print(f"2  {emoji_grid[2][0]}   {emoji_grid[2][1]}   {emoji_grid[2][2]}   {emoji_grid[2][3]}") 
    print(f"3  {emoji_grid[3][0]}   {emoji_grid[3][1]}   {emoji_grid[3][2]}   {emoji_grid[3][3]}")

    print("")
    hidden_grid[e1x][e1y] = emoji_grid[e1x][e1y]
    print("")

    if(emoji_grid[e2x][e2y] == emoji_grid[e1x][e1y]) :
        hidden_grid[e2x][e2y] = emoji_grid[e2x][e2y]
        score+=1



    else :
        hidden_grid[e1x][e1y] = "⬜"
        hidden_grid[e2x][e2y] = "⬜"

    print("    0    1     2    3")

    print(f"0  {hidden_grid[0][0]}   {hidden_grid[0][1]}   {hidden_grid[0][2]}   {hidden_grid[0][3]}") 
    print(f"1  {hidden_grid[1][0]}   {hidden_grid[1][1]}   {hidden_grid[1][2]}   {hidden_grid[1][3]}") 
    print(f"2  {hidden_grid[2][0]}   {hidden_grid[2][1]}   {hidden_grid[2][2]}   {hidden_grid[2][3]}") 
    print(f"3  {hidden_grid[3][0]}   {hidden_grid[3][1]}   {hidden_grid[3][2]}   {hidden_grid[3][3]}") 
    print(score)


memory_game("0,0", "2,1")





