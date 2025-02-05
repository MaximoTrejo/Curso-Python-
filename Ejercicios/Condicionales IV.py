#and (y si ademas) 
#or(o sino)
#in(sirve para iterar sobre una secuencia)

#distancia = int(input("introducir la distancia"))
#numero_hermanos= int(input("introduci el numero de hermanos"))
#sueldo= int(input("introduci el sueldo"))


#ejemplo and
#if(distancia > 40 and numero_hermanos > 2 and sueldo <= 200000):
#    print("tiene beca")
#else:
#    print("no tiene beca")

#ejemplo or
#en este caso si las 2 consiciones no se cumple pero si la del suendo va a pasar 
#if(distancia > 40 and numero_hermanos > 2 or sueldo <= 200000 ):
#    print("tiene beca")
#else:
#    print("no tiene beca")


#ejemplo in
#lower transforma a minusculas
#upper transforma a mayusculas


print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion= input("introduci la asignatura")
asignatura = opcion.lower()
#asignatura = opcion.upper()

if(asignatura in ("informatica grafica - pruebas de software - usabilidad y accesibilidad")):
    #no hace falta el str ya que la variable asignatura ya es un string
    print("asigatura elegida" + str(asignatura))
else:
    print("no se puede")