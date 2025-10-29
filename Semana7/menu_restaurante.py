# Sistema Básico de Restaurante

print("Bienvenido al sistema de gestión de restaurante")

#Creación del restaurante

nombre_restaurante = input("Ingrese el nombre del restaurante: ")

platillos = {}
for i in range(3):
    nombre = input(f"Nombre del platillo {i+1}: ")
    precio = float(input(f"Precio de {nombre}: ₡ "))
    platillos[nombre] = precio
# Lista para guardar las órdenes
ordenes = []
numero_orden = 1

#Menú interactivo

while True:
    print("\n MENÚ PRINCIPAL")
    print("1. Crear una nueva orden")
    print("2. Ver órdenes actuales")
    print("3. Cambiar estado de una orden")
    print("4. Finalizar una orden")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    #Crear una nueva orden
   
    if opcion == "1":
        print("\n Menú del restaurante:")
        for i, (nombre, precio) in enumerate(platillos.items(), start=1):
            print(f"{i}. {nombre} - ₡{precio}")

        seleccion = input("Seleccione los platillos (ejemplo: 1,2 o 1,2,3): ")
        indices = [int(i.strip()) for i in seleccion.split(",")]

        # Crear lista de platillos seleccionados
        nombres_platillos = list(platillos.keys())
        platillos_seleccionados = [nombres_platillos[i-1] for i in indices]

        # Crear orden como diccionario
        orden = {
            "numero": numero_orden,
            "platillos": platillos_seleccionados,
            "estado": "Iniciado"
        }

        ordenes.append(orden)
        print(f" Orden #{numero_orden} creada.")
        numero_orden += 1

    #Ver órdenes actuales
  
    elif opcion == "2":
        if len(ordenes) == 0:
            print("No hay órdenes actualmente.")
        else:
            print("\n Órdenes actuales:")
            for orden in ordenes:
                print(f"Orden #{orden['numero']} - Estado: {orden['estado']} - Platillos: {', '.join(orden['platillos'])}")

    #Cambiar estado de una orden
  
    elif opcion == "3":
        num = int(input("Ingrese el número de la orden: "))
        encontrada = False
        for orden in ordenes:
            if orden["numero"] == num:
                print("Estados: Iniciado / En preparación / Finalizado")
                nuevo_estado = input("Nuevo estado: ")
                orden["estado"] = nuevo_estado
                print(f"Estado de la orden #{num} actualizado a {nuevo_estado}.")
                encontrada = True
                break
        if not encontrada:
            print(" Orden no encontrada.")

    #Finalizar una orden
   
    elif opcion == "4":
        num = int(input("Ingrese el número de la orden a finalizar: "))
        encontrada = False
        for orden in ordenes:
            if orden["numero"] == num:
                total = sum(platillos[n] for n in orden["platillos"])
                print(f"\n Total a pagar por la orden #{num}: ₡{total}")
                ordenes.remove(orden)
                print("Orden eliminada del sistema.")
                encontrada = True
                break
        if not encontrada:
            print(" Orden no encontrada.")

    #Salir
 
    elif opcion == "5":
        print(" Gracias por usar el sistema. ¡Vuelve pronto!")
        break

    else:
        print("Opción inválida, intente nuevamente.")