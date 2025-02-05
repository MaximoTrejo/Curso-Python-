salario_presidente = int(input("introduzca el salario del presidente"))
print("Salario: " + str(salario_presidente))

salario_director = int(input("introduzca el salario del director "))
print("Salario: " + str(salario_director))

salario_jefe_area = int(input("introduzca el salario del jefe_area"))
print("Salario: " + str(salario_jefe_area))


if(0<salario_jefe_area<salario_director<salario_presidente):
    print("bien")
else:
    print("algo salio mal")