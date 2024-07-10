#Ejercicio 12: Escribe un programa que invierta una cadena introducida por el usuario.

cadena = input("Introduce una cadena: ")

cadena_invertida = ""

for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print(f"La cadena invertida es: {cadena_invertida}")