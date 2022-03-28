import math
import re

def solveEquation(equation):
    str = re.split('x²+|x|=|\*|\n',equation)
    
    if not str[0]: str[0]=1

    if not str[1] or str[1]=="+" : str[1]=1

    a = int(str[0])
    b = int(str[1])
    c = int(str[2])
 
    delta = (math.pow(b,2))-4*a*c
    x_positive = round((-b + math.sqrt(delta))/(2*a),2)
    x_negative = round((-b - math.sqrt(delta))/(2*a),2)

    result = (f"Resultado da equação de 2º grau {equation}:\nx+ = {x_positive}\nx- = {x_negative}\n")
    return result


print(solveEquation("x²+12x-13=0"))
print(solveEquation("2x²+16x-18=0"))
print(solveEquation("x²+x-6=0"))