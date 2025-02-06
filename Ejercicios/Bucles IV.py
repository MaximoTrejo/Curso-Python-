#i=1

#while i<= 10:
#    print("Ejecucion " + str(i))
#    i += 1 # o i= i +1

#print("Termino el programa")

#edad = int(input("ingresa tu edad"))

#while edad < 0 or edad > 100:
#    print("volve a intentarlo")
#    edad = int(input("Ingresa tu edad"))

#print("edad ingresada" + str(edad))


import math


numero = int(input("ingresa un numero"))
intentos=0

while numero < 0 :
    print("volve a intentarlo")
    if(intentos == 2):
        print("sos un gil, el programa termino")
        break;
    
    numero = int(input("ingresa un numero"))
    if(numero < 0):
        intentos +=1

if(intentos < 2):
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es " + str(solucion) )

