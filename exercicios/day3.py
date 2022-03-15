
# Calculadora de IMC com retorno de múltiplas alternativas
def imcCalc(peso, altura):
    pesoF = float(peso)
    alturaF = float(altura)
    imc = pesoF/(alturaF**2)
    result = round(imc, 2)
    
    if(result<18.5):
        message = f"Seu IMC é de {result}: Abaixo do peso"
    elif(result >= 18.50 and result <= 25.0):
        message = f"Seu IMC é de {result}: Peso ideal"
    elif(result >25,0 and result < 30.0):
        message = f"Seu IMC é de {result}: Acima do peso"
    elif(result >30,0 and result < 35.0):
        message = f"Seu IMC é de {result}: Obesidade"
    else:
        message = f"Seu IMC é de {result}: Obesidade mórbida"
        
    print(message)


    


print("Bem-vindo à calculadora de gordo")
altura = input("Altura: ")
peso = input("Peso: ")

resultIMC = imcCalc(peso, altura)

print(resultIMC)


#Calculadora de ano bissexto:
def anoBissexto(ano):
    anoInt = int(ano)
    if(anoInt%4==0): 
        if anoInt%100==0 and not anoInt%400==0:
           return f"{ano} não é bissexto"
        else:
           return f"{ano} é bissexto"
    else:
        return f"{ano} não é bissexto"
        
    
print(anoBissexto(400))
print(anoBissexto(500))
print(anoBissexto(600))
print(anoBissexto(800))
print(anoBissexto(1200))
print(anoBissexto(1500))
print(anoBissexto(1700))
print(anoBissexto(1800))
print(anoBissexto(1900))
print(anoBissexto(2000))
print(anoBissexto(2022))
print(anoBissexto(2024))
print(anoBissexto(2100))
print(anoBissexto(2300))
print(anoBissexto(2400))
