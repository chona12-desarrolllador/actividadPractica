nombre = input("Ingrese el nombre:")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
suma = nota1+nota2+nota3
promedio = suma/3
if promedio >=7 :
    mensaje="Promocionado"
else:
    if promedio >= 4 :
        mensaje="Regular"
    else:
        mensaje="Reprobado"