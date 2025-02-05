#primera parte

print("Programa de evaluacion")

#siempre lo toma como un string, en caso de introducir un numero hay que castearlo
nota_alumno=input("Nota del alumno: ")

def evaluacion(nota):
    valor="aprobado"
    if(nota < 5 ):
        valor="desaprobado"
    return valor

print(evaluacion(int(nota_alumno)))
