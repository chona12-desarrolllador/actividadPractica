nota1=float(input("ingrese la primera nota: "))
nota2=float(input("ingrese la segunda nota: "))
nota3=float(input("ingrese la tercera nota: "))

promedio = (nota1+nota2+nota3)/3
print("el promedio de las notas es: ", promedio)

if promedio>=3.5:
    print("el estudiante aprueba la materia")
else:
    print("perdio de ñengo flow")