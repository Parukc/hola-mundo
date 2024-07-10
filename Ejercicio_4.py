#Ejercicio 4: Escribe un programa que realice operaciones básicas (suma, resta, multiplicación y división) entre dos números introducidos por el usuario
num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese el segundo numero "))

print("Ingrese la operaciòn que desee realizar")
print("1, suma")
print("2, resta")
print("3, multiplicacion")
print("4, division")

operacion = input("Ingresa la opcion de la operacion ")

if operacion == "1":
  resultado = num1 + num2
  print(f"La suma total de {num1} y {num2} es igual a {resultado} ")
elif operacion == "2":
  resultado = num1 - num2
  print(f"La resta total de {num1} y {num2} es igual a {resultado} ")
elif operacion == "3":
  resultado = num1 * num2
  print(f"La multiplicacion total de {num1} y {num2} es igual a {resultado} ")
elif operacion == "4":
  resultado = num1 / num2
  print(f"La division total de {num1} y {num2} es igual a {resultado} ")
else:
  print("Introducir un valor valido")