#----------------------------------------------------

print("verificacion de edad")

edad = int(input("introduce la edad"))

if(edad < 18):
    print("no pasa") 
#esto se activa cuando lo se cumple la condicion del if pero tampoco el else
elif (edad > 100):
    print("incorrecto")
else:
    print("pasa") 

print("programa finalizado")       
