mutant_rawdata = """Fish, 15959, 79, 98, 2, 4
Crystal, 339113, 786, 923, 17, 249
Eyes, 72952, 241, 285, 3, 52
Melting, 22653, 234, 248, 2, 2
Plant, 6019, 51, 68, 1, 1
Y.V., 18092, 81, 97, 0, 10
Steroids, 12066, 48, 61, 1, 4
Robot, 8466, 41, 46, 1, 2
Chicken, 9172, 35, 47, 3, 3
Rebel, 19640, 80, 93, 1, 7
Horror , 9063, 42, 52, 1, 1
Rogue, 43832, 285, 314, 1, 8"""

mutant_list = mutant_rawdata.split("\n")
ranked = []
for mutant in mutant_list :
    mutant_data = (mutant.split(", "))
    ranked.append(mutant_data)



max_kills = 0
max_deaths = 0
win_percent_max = 0

killed_most = ""
died_most = ""
best_win_ratio = ""

output_list = ""

for n in range(len(ranked)):
    mutant = ranked[n]

    kills = int(mutant[1])
    deaths = int(mutant[2])
    runs = (int(mutant[3]))
    wins = (int(mutant[4])+int(mutant[5]))


    win_percent= float(round((wins/runs) * 100, 2))
    mutant.append(win_percent)

    if kills >= max_kills:
        max_kills = kills
        killed_most = f"Most kills: \n\t{mutant[0]}:  {mutant[1]} enemies killed"

    if deaths >= max_deaths:
        max_deaths = deaths
        died_most = f"Died most: \n\t{mutant[0]}: {mutant[2]} free trips back to the Campfire"
    
    if win_percent >win_percent_max :
        win_percent_max = win_percent
        best_win_ratio = f"Best % of successful runs (win/loop): \n\t{mutant[0]}: {mutant[6]}%"

    
    output_list += f"""
    {mutant[0]}\t{mutant[1]}\t{mutant[2]}\t{mutant[3]}\t{mutant[4]}\t{mutant[5]}\t{mutant[6]}%
    """
    
print("Nuclear Throne Ranking and Character Data:")
    
print(f"""
    Best Score:
    \t{killed_most}
    \t{died_most}
    \t{best_win_ratio}
""")
print("""
Character\tKills\tDeaths\tRuns\tWins\tLoop\tWin%(loops+wins)
""")

print(output_list)





