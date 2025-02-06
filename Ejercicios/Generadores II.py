#el * en una funcion sirve para indicarle que lo que recibe puede se una lista , 
# una tupla  
#con esto ingreso a las letras de las cuidades
def devuelve_cuidades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            #yield subElemento
            #con yield from nos ahorramos de hacer el buple para entrar a los elementos de un elemento
            yield from elemento

cuidades_devueltas = devuelve_cuidades("Madrid","Barcelona","bilbao","valencia")

#el next te devuelve de a uno los elementos
print (next(cuidades_devueltas))
print (next(cuidades_devueltas))