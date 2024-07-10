#Ejercicio 11: Escribe un programa que sume todos los números naturales hasta un número límite introducido por el usuario.

limite = int(input("Introduce el número límite: "))

suma = 0
for i in range(1, limite + 1):
    suma += i

print(f"La suma de los números naturales hasta {limite} es {suma}")