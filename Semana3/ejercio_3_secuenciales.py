# Declaracion de variables

peso=0.0
altura=0.0
nombre=""
imc= 0.0


# Entrada de datos

nombre = input("ingrese su nombre: ")
peso = float (input("ingrese el paso en kg: "))
altura = float (input("ingrese el altura en metros: "))

                    
# Operaciones

imc= peso / altura **2


# Salida de datos

print(f"Hola {nombre}!,su IMC es  de {imc}")

print(f"Hola {nombre}!,su IMC es  de {imc:.2f}")
