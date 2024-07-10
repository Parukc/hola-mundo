#Ejercicio 14: Escribe un programa que determine si una cadena introducida por el usuario es un palíndromo.

cadena = input("Introduce una cadena: ")
es_palindromo = True
for i in range(len(cadena) // 2):
    if cadena[i] != cadena[len(cadena) - i - 1]:
        es_palindromo = False
        break
if es_palindromo:
    print(f"La cadena {cadena} es un palíndromo.")
else:
    print(f"La cadena {cadena} no es un palíndromo.")