#Ejercicio 13: Escribe un programa que cuente el número de vocales en una cadena introducida por el usuario.

cadena = input("Introduce una cadena: ")
vocales = 0
for letra in cadena:
    if letra in "aeiouAEIOU":
        vocales += 1
print(f"La cadena tiene {vocales} vocales.")