# Sistema Básico de Restaurante

print("Bienvenido al sistema de gestión de restaurante")

#Creación del restaurante

nombre_restaurante = input("Ingrese el nombre del restaurante: ")

platillos = {}
for i in range(3):
    nombre = input(f"Nombre del platillo {i+1}: ")
    precio = int(input(f"Precio de {nombre}: ₡ "))
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
        for i, (nombre, precio) in enumerate(platillos.items(), start=1):   #El método .items() devuelve (nombre, precio) de cada platillo
            print(f"{i}. {nombre} - ₡{precio}")

        seleccion = input("Seleccione los platillos (ejemplo: 1,2,3): ")
        indices = [int(i.strip()) for i in seleccion.split(",")]        #split: Divide la cadena de texto en partes cada vez que encuentra una coma
                        #El método .strip() elimina los espacios al principio o final de cada número

        # Crear lista de platillos seleccionados
        nombres_platillos = list(platillos.keys())   #El método .keys() devuelve los nombres de los platillos
        platillos_seleccionados = [nombres_platillos[i-1] for i in indices] # i-1: Devuelve el nombre del platillo que está en esa posición

        # Crear orden como diccionario
        orden = {
            "numero": numero_orden,
            "platillos": platillos_seleccionados,
            "estado": "Iniciado"
        }

        ordenes.append(orden)   #El método .append() agrega la nueva orden a la lista de órdenes
        print(f" Orden #{numero_orden} creada.")    #f-string: Incluye el número de orden dentro del texto
        numero_orden += 1   #Aumentador del número de orden para la próxima orden

    #Ver órdenes actuales
  
    elif opcion == "2":
        if len(ordenes) == 0:       #len(): Devuelve la cantidad de elementos en la lista
            print("No hay órdenes actualmente.")
        else:
            print("\n Órdenes actuales:")
            for orden in ordenes:
                print(f"Orden #{orden['numero']} - Estado: {orden['estado']} - Platillos: {', '.join(orden['platillos'])}")
                    #El método .join(): Une los nombres de los platillos en una sola cadena separada por comas

    #Cambiar estado de una orden
  
    elif opcion == "3":
        num = int(input("Ingrese el número de la orden: "))
        encontrada = False      #Verifica si la orden fue encontrada, se inicia en False para saber si se encontró o no
        for orden in ordenes:
            if orden["numero"] == num:
                print("Estados: Iniciado / En preparación / Finalizado")
                nuevo_estado = input("Nuevo estado: ")
                orden["estado"] = nuevo_estado
                print(f"Estado de la orden #{num} actualizado a {nuevo_estado}.")
                encontrada = True #Cambiamos a True si se encontró la orden
                break
        if not encontrada:
            print(" Orden no encontrada.")

    #Finalizar una orden
   
    elif opcion == "4":
        num = int(input("Ingrese el número de la orden a finalizar: "))
        encontrada = False
        for orden in ordenes:
            if orden["numero"] == num:
                total = sum(platillos[n] for n in orden["platillos"])   #Suma los precios de los platillos en la orden
                print(f"\n Total a pagar por la orden #{num}: ₡{total}")
                ordenes.remove(orden)   #El método .remove() elimina la orden de la lista
                print("Orden eliminada del sistema.")
                encontrada = True   #Marcamos como True si se encontró la orden y se sale del ciclo
                break
        if not encontrada:
            print(" Orden no encontrada.")

    #Salir
 
    elif opcion == "5":
        print(" Gracias por usar el sistema. ¡Vuelve pronto!")
        break

    else:
        print("Opción inválida, intente nuevamente.")