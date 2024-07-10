#Ejercicio 15: Escribe un programa que calcule el factorial de un número introducido por el usuario.

num = int(input("Introduce un número: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es {factorial}")