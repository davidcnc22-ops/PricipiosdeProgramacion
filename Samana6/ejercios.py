""" 6. Imprimir los números impares entre dos valores
o Recibe dos números A y B (con A < B) e imprime todos los números
impares en ese rango.


# Ejercicio 6: Imprimir los números impares entre dos valores

A = int(input("Ingrese el valor de A (menor): "))
B = int(input("Ingrese el valor de B (mayor): "))

if A < B:
    print(f"Los números impares entre {A} y {B} son:")
    for numero in range(A, B + 1):
        if numero % 2 != 0:
            print(numero)
else:
    print("Error: El valor de A debe ser menor que el de B.")
 """

""" # Ejercicio 7: Calcular el factorial de un número
N = int(input("Ingrese un número entero positivo: "))
if N >= 0:
    factorial = 1

    for i in range(1, N + 1):
        factorial *= i 

    print(f"El factorial de {N} es: {factorial}")
else:
    print("Error: Debe ingresar un número entero positivo.") """

""" Ejercio

numero = int(input("Ingrese un número estero positivo: "))


if numero> 0:
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    print(f"La suma de los digítos es: {suma}")
else:
    print("Error, se debe ingresar un número entero positivo") """

""" # Ejercicio 9: Encontrar el mayor de un conjunto de números
Pedir la cantidad de números
Verificar que la cantidad sea positiva
leer los N números
numero = int(input("Ingrese el numero a comparar: "))
if numero > 0:
    mayor = None

    for i in range(numero):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        if mayor is None or numero > mayor:
            mayor = numero

    print(f"El número mayor es: {mayor}") """

""" N = int(input("Ingrese un número entero positivo: "))

if N > 1:
    es_primo = True

    for i in range(2, N):
        if N % i == 0:
            es_primo = False
            break 
    if es_primo:
        print(f"{N} es un número primo.")
    else:
        print(f"{N} no es un número primo.")
else:
    print("El número debe ser mayor que 1.") """

""" # Ejercicio 11: Invertir un número

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    invertido = 0

    while numero > 0:
        digito = numero % 10           
        invertido = invertido * 10 + digito  
        numero //= 10                  

    print(f"El número invertido es: {invertido}")
else:
    print("Error: Debe ingresar un número entero positivo.") """

""" # Ejercicio 11: Invertir un número

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    invertido = 0

    while numero > 0:
        digito = numero % 10           
        invertido = invertido * 10 + digito  
        numero //= 10                  

    print(f"El número invertido es: {invertido}")
else:
    print("Error: Debe ingresar un número entero positivo.") """

""" # Ejercicio 12: Imprimir los primeros N números de la serie Fibonacci

N = int(input("Ingrese la cantidad de números de la serie Fibonacci: "))

if N > 0:
    a, b = 0, 1  
    print("Serie Fibonacci:")

    for i in range(N):
        print(a)
        a, b = b, a + b  
else:
    print("Error: Debe ingresar un número positivo.") """


