    #Calculadora de altura média (usando for loop):


def alturaMedia(lista):
    altura_alunos =  lista.split()
    type(altura_alunos)
    


    soma_alturas = 0
    media_alturas = 0
    mais_alto = 0
    mais_baixo = 0
    qtde_alunos = 0
    for altura in altura_alunos:
        altura_int = int(altura)
        soma_alturas+=altura_int
        
        qtde_alunos+=1
        if altura_int > mais_alto :
            mais_alto = altura_int
    altura_alunos.sort()

    mais_baixo = int(altura_alunos[0])
    
    media_alturas = round(soma_alturas / qtde_alunos)
    return f"""
    \nMédia de altura entre {qtde_alunos} alunos: {media_alturas}cm
    \nMaior altura: {mais_alto}  - {mais_alto - media_alturas}cm acima da média
    \nMenor altura: {mais_baixo}  - {media_alturas - mais_baixo}cm abaixo da média"""

print(alturaMedia("122 123 150 178 195 170 175"))


#################################################


#Ranking de melhor pontuação entre alunos: 
def highscore(students) :
    final_ranking = ""
    best_score = 0
    best_student = ""
    student_list = students.split(", ")
    ranking = []
    for student in student_list:
        student_data = student.split(": ")
        ranking.append(student_data)

    
    for n in range(len(ranking)) :
        ranking[n][1] = int(ranking[n][1])
        
    ranking.sort(key=lambda x: x[1], reverse=True)


    for n in range(len(ranking)) :
        wizard = ranking[n]
        if wizard[1] > best_score:
            best_score = wizard[1]
            best_student = wizard[0]

        final_ranking += f"{n+1}. {wizard[0]} - {wizard[1]} pontos\n"
    
    final_ranking += f"\nParabéns {best_student} pela maior pontuação este ano!\n"

    return final_ranking


grifinoria = "Harry Potter: 100, Ronald Weasley: 75, Hermione Granger: 150, Neville Longbottom: 10, Dean Thomas: 50, Lavanda Brown: 35"

print("\nAlunos que mais pontuaram pela Grifinória:")
print(highscore(grifinoria))


#################################################


#Cálculo de Gauss (soma de todos os números de 1 a 100):
n = 0
n_string= ""
for x in range(1,101):
    n+=x
    print(f"+{x} = {n}, ")
print("\n")

#################################################

#Cálculo de Gauss(apenas números pares):
p = 0
p_string= ""
for x in range(2,101):    
    if x%2==0:
        p+=x
        print(f"+{x} = {p}, ")
print("\n")

#FizzBuzz
for n in range (1,101):
    if n %3==0 and n%5==0:
        print(f"{n}, FizzBuzz, {n/15}")
    elif n%3==0:
        print(f"{n}, Fizz, {n/3}")
    elif n%5==0:
        print(f"{n}, Buzz {n/5}")
    else:
        print(n)







#Texto truncado:
text = "abcdefgh"
truncated_text = text[0:4]

print(truncated_text)


