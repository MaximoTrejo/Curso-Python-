#las tuplas son como las listas pero nose modifican
tupla=("1","2","3","1")
#se puede generar una lista en base a una tupla
miLista= list(tupla)
#nos damos cuenta que es una tupla o una lista es por los [](lista) ()tupla
print(miLista)
#tambien se puede transformar una lista en una tupla 
Tupla2= tuple(miLista)
#se puede contar cuantos elementos hay de algo
print (Tupla2.count("1"))
#se puede saber cuentos elementos tiene una tupla 
print(len(Tupla2))
#python asigna directamente los datos de una tupla a una variable
tuplaPrueba =("maxi",2002,3,16)
nombre,año,mes,dia =tuplaPrueba
print(nombre),print(año),print(mes),print(dia) 

print(Tupla2)
print(tupla)
print(tupla[2])