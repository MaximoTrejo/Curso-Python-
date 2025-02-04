Lista=["maxi","pepe","nico","mario"]

#para mostrar solo un elemento nos manejamos con indices 
print(Lista[0])
#podes acceder a una porcion de la lista
print(Lista[0:3])#con el 0 le indico cual no quiero 

#agrega el elemento al final
Lista.append("masi2")
#agrega en la posicion que quieras
Lista.insert(2,"fideo")
#agregar datos de otra lista o varios elementos a mi lista
Lista.extend(["rocio","pepe","feo"])
#saber el indice de un elemento
print(Lista.index("rocio"))
#saber si el elemento esta en la lista
print("pepe" in Lista)
#eliminar elementos de la lista
Lista.remove("maxi")
#Se pueden sumar listas para unirlas sin necesidad de usar el extend 
Lista2=["sandra","lucia"]
Lista3 = Lista + Lista2

print(Lista3)
print(Lista)
