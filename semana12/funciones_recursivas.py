""" def cuenta_regresiva(n):
    #Caso base: cuando n llegue a 0, detenemos la recursion
    if n == 0:
        return
    print(n)
    cuenta_regresiva(n - 1)

cuenta_regresiva(10) """

numeros = []

def cuenta_regresiva(n):
    if n == 0:
        print(0)
        numeros.append(0)
        return
    numeros.append(n)
    print(n)
    if n > 0:
        cuenta_regresiva(n - 1)
    else:
        cuenta_regresiva(n + 1)

n = int(input("Ingrese un número entero (positivo o negativo): "))
cuenta_regresiva(n)

print("Lista generada:", numeros)