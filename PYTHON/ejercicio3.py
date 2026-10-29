cedula = input("ingrese el numero de su cedula: ")
nombre = input("ingrese su nombre: ")
salario = int(input("ingrese su salario mensual: "))
horas_trabajadas = int(input("ingrese el numero de horas que trabajo: "))

valorHora = salario/210

ValoraPagar = valorHora * horas_trabajadas

print(".........colilla de nomina................")
print("         cedula" , cedula)
print(f"        nombre: {nombre}")
print("..........................................")
print(f"Basico Mensual :{salario} ")
print(f"horas trabajadas: {horas_trabajadas}")
print(f"valor hora: {valorHora}")
print(f"valor a pagar: {ValoraPagar}")
