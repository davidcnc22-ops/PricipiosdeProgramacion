def  mostrar_menu():
    print("\nMenú:")
    print("1. Cargar información")
    print("2. Agregar teléfono")
    print("3. Eliminar teléfono")
    print("4. Procesar venta")
    print("5. Generar reporte")
    print("6. Salir")


def main():
    print("Bienvenido al sistema de venta de celulares")
    mostrar_menu()

    opcion = input("Por favor ingrese una opción del 1 al 6: ")

    if opcion == '1':
        print(" Mostrando lista de teléfonos disponibles...")
    elif opcion == '2':
        print(" Agregando un nuevo teléfono al sistema...")
    elif opcion == '3':
        print(" Eliminando un teléfono del inventario...")
    elif opcion == '4':
        print(" Procesando una venta...")
    elif opcion == '5':
        print(" Generando reporte de ventas...")
    elif opcion == '6':
        print(" Saliendo del sistema, ¡hasta pronto!")
    else:
        print(" Opción no válida. Por favor ingrese un número del 1 al 6.")


if __name__ == "__main__":
    main()
 



