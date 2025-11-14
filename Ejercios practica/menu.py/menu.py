menu= "" \
    "1. Validar número entero (0/20) y analizar estado del juego\n" \
    "2. Validar número entero (0/50) y calcular puntos acumulados\n" \
    "3. Validar carácter (o, l, s, z, L, J, T) y mostrar figura con asteriscos\n" \
    "4. Ingrese un numero valido\n" \
    "0. Salir del programa" 

print(menu)

opcion = int(input("Ingrese la opción del menú: "))

while opcion!=0:
        if opcion == 1:
            print("Validar número entero (0/20) y analizar estado del juego")
        elif opcion == 2:
            print("Validar número entero (0/50) y calcular puntos acumulados")
        elif opcion == 3:
            print("Validar carácter (o, l, s, z, L, J, T) y mostrar figura con asteriscos")
        elif opcion == 4:
            print("Ingrese un número válido")
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        opcion = int(input("Ingrese la opción del menú: "))
    
        print("Entrada inválida. Debe ingresar un número entero.")