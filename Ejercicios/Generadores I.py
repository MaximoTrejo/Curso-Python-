#ventaja de los generadores es que en caso que se necesite un numero de una lista no
#hace falta generar la lista entera, esto es asi porque lo devuelve de uno a uno 
def generaPares(limite):
    num=1

    while num< limite:
        #construye un objeto iterabble que lo amacena y lo devuelve 1 en 1 
        yield num*2
        num += 1

devuelvePares=generaPares(10)

print(next(devuelvePares))
print("---------------------------------")
print(next(devuelvePares))
print("---------------------------------")
print(next(devuelvePares))

#for i in devuelvePares:
#    print(i)



    
