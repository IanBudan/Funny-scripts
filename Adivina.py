import random

numero = random.randint(1, 10)

print("Se generaran numeros del uno al diez. Adivina!")
respuesta = int(input("Numero:"))

if respuesta == numero:
     print ("Acertaste!")
else:
     print (f" Oh, no lo hiciste, el numero correcto era {numero}")

