#for letra in "python":
#    if(letra== "h"):
#        continue
#    print("letra " + letra)


#contador= 0
#nombre= "pildoras informaticas"
#for letra in nombre:
#    if(letra== " "):
#        continue
#    contador += 1
    
#print(str(contador))


email=input("introduce tu email ")

for i in email:
    if(i=="@"):
        arroba=True
        break;
else:
    arroba = False

print(arroba)