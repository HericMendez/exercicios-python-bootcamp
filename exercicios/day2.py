
#recebe input de dois dígitos, e então soma o primeiro dígito com o segundo:

n= input("Number:")

c1 = int(n[0])
c2 = int(n[1])

new_n = c1+c2


print(f"sum {new_n}")


#Caculadora de IMC:
def imcCalc(peso, altura):
    imc = float(peso)/(float(altura)**2)
    result = str(round(imc, 2))
    return result


print(imcCalc(120, 1.5))



#Calcula o seu tempo restante de vida, assumindo que você viverá até os 90 anos de idade.
def tempoRestante(idade):
    dias_90_anos = 32850
    semanas_90_anos = 4680
    meses_90_anos = 1080
    
    dias_restantes = dias_90_anos - (365*int(idade))
    semanas_restantes = semanas_90_anos - (52*int(idade))
    meses_restantes = meses_90_anos - (12*int(idade))
    
    result = f"Você tem {dias_restantes} dias, {semanas_restantes} semanas e {meses_restantes} restantes de vida."
    return result


idade_int = int(input("qual é sua idade?"))
print(tempoRestante(idade_int))


#Calculadora de gorjeta:
def tipCalc(total, tip, numPeople):
    totalF = float(total)
    tipF = int(tip)
    numPeopleInt = int(numPeople)
    tipPercent = round(totalF*(tip/100), 2)
    billWithTip = round(totalF+tipPercent, 2)
    sharedBill = round(billWithTip / numPeopleInt, 2)
    message = f"Total with tip of {tip}% (${tipPercent}): ${billWithTip}\nEach person must pay ${sharedBill}"
               
    
    return message
    

print("Welcome to the tip calculator.")
totalInput = float(input("What's the total of the bill?"))
print(type(totalInput))
tipInput = float(input("What's the tip's percentage to the waiter? (10, 12, 15)"))
peopleInput = float(input("How many people will share the bill?"))



print(tipCalc(totalInput, tipInput, peopleInput))
