
#Verificador de número primo:
def prime_checker(num):
    modulo = []
    for n in range(2, num):
        modulo.append(num%n)
        
    if 0 in modulo:
        print(f"Number {num} is not prime")
    else:
        print(f"Number {num} is prime")
    
    
prime_checker(7)
prime_checker(8)
prime_checker(96)
prime_checker(97)