#Ejercicio 17: Escribe un programa que calcule el índice de masa corporal (IMC) a partir del peso y la altura introducidos por el usuario.

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Tu IMC es {imc:.2f}. Tienes bajo peso.")
elif 18.5 <= imc < 25:
    print(f"Tu IMC es {imc:.2f}. Tienes un peso normal.")
elif 25 <= imc < 30:
    print(f"Tu IMC es {imc:.2f}. Tienes sobrepeso.")
else:
    print(f"Tu IMC es {imc:.2f}. Tienes obesidad.")