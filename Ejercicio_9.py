#Ejercicio 9: Escribe un programa que muestre la tabla de multiplicar de un número introducido por el usuario.
numero_ingresado_usuario = int(input("Ingrese un numero "))
print("la tabla del", numero_ingresado_usuario)
for i in range(1, 11):
  resultado = numero_ingresado_usuario * i
  print(f"{numero_ingresado_usuario} x {i} = {resultado}")