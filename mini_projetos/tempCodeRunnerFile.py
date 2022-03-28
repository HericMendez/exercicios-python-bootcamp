def caesars_cypher(input_txt, shift, cmd):
    letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'    
    lista_abc = letras.split(' ')
    p=0

    msg = input_txt.lower()
    
    if cmd =="encrypt":
        p=shift
    elif cmd=="decrypt":
        p=shift*-1
    else:
        return print(f"[ERRO] Comando inválido: '{cmd}'")

    if p>26: p=p%26

    part1 = lista_abc[0:p]
    part2 = lista_abc[p:26]
    lista_enc = part2+part1
    new_msg=""
    
    for n in range(len(msg)):
        if msg[n] in lista_abc:
            abc_index = lista_abc.index(msg[n])
            new_msg+=lista_enc[abc_index]
        else:
            new_msg+=msg[n]
        
    return new_msg


print(34%26)

#encrypt command:
print("\nencrypt command:\n", caesars_cypher("gabriel eh gay", 34, "encrypt")) 

#decrypt command:
print("\ndecrypt command:\n", caesars_cypher("zwvitlqvpw awkkmz 98", 8, "decrypt"), "\n") 