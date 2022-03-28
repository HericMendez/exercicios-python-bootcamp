import random

def passwordGenerator(lth):
    letras = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    numeros = '0 1 2 3 4 5 6 7 8 9'
    simbolos = '! @ # $ % & * ( ) +'

    nova_senha=""

    lista_abc = letras.split(' ')
    lista_num = numeros.split(' ')
    lista_sim = simbolos.split(' ')

    random.shuffle(lista_abc)
    random.shuffle(lista_num)
    random.shuffle(lista_sim)

    qtde_letras = random.randint(round(lth/4),round(lth*0.6))

    qtde_numeros = random.randint(round(lth/4),round(lth/3))
    qtde_simbolos = lth-(qtde_letras+qtde_numeros)
    letras_senha = lista_abc[0:qtde_letras]
    numeros_senha = lista_num[0:qtde_numeros]
    simbolos_senha = lista_sim[0:qtde_simbolos]

    caracteres_mix = letras_senha+numeros_senha+simbolos_senha
    random.shuffle(caracteres_mix)
    if lth<8 or lth>32:
        nova_senha = "[ERRO]A senha deve ter entre 8 a 32 caracteres!"
    else:
        for caractere in caracteres_mix:
            nova_senha+=caractere


    return nova_senha



print("Teste com 3 caracteres:\n ", passwordGenerator(3))
print("")
print("Teste com 33 caracteres:\n ",passwordGenerator(33))
print("")
print("Teste com 8 caracteres:\n",passwordGenerator(8))
print("")
print("Teste com 32 caracteres:\n",passwordGenerator(32))
print("")
print("Teste com 12 caracteres:\n ",passwordGenerator(12))


