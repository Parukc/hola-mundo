#Ejercicio 5: Escribe un programa que pida tres números al usuario y determine cuál es el mayor.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print(f"El número mayor es: {mayor}")