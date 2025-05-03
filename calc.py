#This script works like a CLI calculator with basic operations like +, -, x and :
#No libraries are needed here
primer = int(input("Primer numero:"))
signo1 = input("Operacion? (+ - * /):")
segundo = int(input("Segundo numero:"))
if signo1 == '+':
    resultado = primer + segundo
elif signo1 == '-':
    resultado = primer - segundo
elif signo1 == '*':
    resultado = primer * segundo
elif signo1 == '/':
    resultado = primer / segundo
else:
    print("Ve a la escuela y aprende matematicas")
print(resultado)    

