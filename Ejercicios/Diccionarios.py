#se manejan usando clave:valor
miDiccionario={"argentina":"buenosAires","alemania":"berlin","españa":"madrid","reino Unido":"londres"}
print(miDiccionario["españa"])

#agregar elementos
miDiccionario["Italia"]="lisboa"
print(miDiccionario)

#modificar elementos
miDiccionario["Italia"]="roma"
print(miDiccionario)

#eliminar un elemento
del miDiccionario["reino Unido"]
print(miDiccionario)

#puedo guardar tuplas dentro de diccionarios
miDiccionario2 = {23:"jordan","nombre":"michael","Equipo":"chicago","anillos":[1991,1992,1993,1994,1995]}
print(miDiccionario2)
#si quiero saber un dato exacto
print(miDiccionario2["anillos"])

#se pueden guardar diccionarios destro de disccionarios
#en este ejemplo en la clave anillos tienen un diccionario con la clave temporadas que tiene el valor que es un tupla con los años
miDiccionario3 = {23:"jordan","nombre":"michael","Equipo":"chicago","anillos":{"temporadas":[1991,1992,1993,1994,1995]}}
print(miDiccionario3["anillos"])

#se puede saber las claves 
print(miDiccionario3.keys())
#se puede saber los valores
print(miDiccionario3.values())

#se puede saber la longitud 
print(len(miDiccionario3))
