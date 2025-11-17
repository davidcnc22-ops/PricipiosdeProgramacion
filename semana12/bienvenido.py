import random
import os

# Lista de diccionarios que almacena los celulares en memoria
celulares = []
archivo_global = "celulares.txt"

def crear_archivo_inicial(nombre_archivo):
    """Crea un archivo inicial con 22 modelos de celulares si no existe"""
    if not os.path.exists(nombre_archivo):
        datos_iniciales = [
            "101,Apple,iPhone 13,799.0,10",
            "102,Apple,iPhone 12,599.0,8",
            "103,Apple,iPhone SE,399.0,5",
            "201,Samsung,Galaxy S23,899.0,12",
            "202,Samsung,Galaxy S22,699.0,7",
            "203,Samsung,Galaxy A54,349.0,15",
            "301,Xiaomi,Redmi Note 12,229.0,20",
            "302,Xiaomi,Mi 11,499.0,6",
            "303,Xiaomi,Mi 12T,429.0,9",
            "401,Huawei,P50 Pro,799.0,4",
            "402,Huawei,Mate 40,699.0,3",
            "501,Google,Pixel 7,599.0,9",
            "502,Google,Pixel 6a,349.0,11",
            "601,Motorola,Moto G Power,199.0,18",
            "602,Motorola,Moto Edge 30,449.0,5",
            "701,OnePlus,OnePlus 11,699.0,7",
            "801,Sony,Xperia 5,749.0,2",
            "901,Nokia,G50,179.0,14",
            "1001,LG,Velvet,399.0,4",
            "1101,Realme,Narzo 50,149.0,22",
            "1201,Oppo,Find X5,799.0,3",
            "1301,Asus,ROG Phone 6,999.0,2"
        ]
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for linea in datos_iniciales:
                archivo.write(linea + "\n")
        print(f"✓ Archivo '{nombre_archivo}' creado con 22 modelos iniciales.\n")

def cargar_informacion(nombre_archivo):
    global celulares
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            celulares = []
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    if len(partes) == 5:
                        celulares.append({
                            "id": int(partes[0]),
                            "marca": partes[1],
                            "modelo": partes[2],
                            "precio": float(partes[3]),
                            "stock": int(partes[4])
                        })
        print(f"✓ Información cargada correctamente. Total: {len(celulares)} celulares.\n")
        mostrar_celulares()
    except FileNotFoundError:
        print("✗ El archivo no existe. Se creará uno al guardar.\n")
        celulares = []
    except ValueError as e:
        print(f"✗ Error al procesar datos: {e}\n")
        celulares = []

def guardar_automaticamente(nombre_archivo):
    """Guarda automáticamente los cambios en el archivo"""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for cel in celulares:
                linea = f"{cel['id']},{cel['marca']},{cel['modelo']},{cel['precio']},{cel['stock']}\n"
                archivo.write(linea)
    except Exception as e:
        print(f"✗ Error al guardar automáticamente: {e}\n")

def mostrar_celulares():
    if not celulares:
        print("✗ No hay celulares cargados.\n")
        return
    print("\n" + "="*90)
    print(f"{'ID':<8} {'Marca':<15} {'Modelo':<25} {'Precio':<12} {'Stock':<8}")
    print("="*90)
    for cel in celulares:
        print(f"{cel['id']:<8} {cel['marca']:<15} {cel['modelo']:<25} ${cel['precio']:<11.2f} {cel['stock']:<8}")
    print("="*90 + "\n")

def existe_celular(marca, modelo):
    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():
            return True
    return False

def obtener_id_unico():
    """Genera un ID único entre 1 y 5000"""
    ids_existentes = {cel["id"] for cel in celulares}
    while True:
        nuevo_id = random.randint(1, 5000)
        if nuevo_id not in ids_existentes:
            return nuevo_id

def agregar_stock():
    print()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    if existe_celular(marca, modelo):
        print("✗ Ya existe un celular con esa marca y modelo.\n")
        return

    try:
        precio = float(input("Precio: $"))
        if precio < 0:
            print("✗ El precio no puede ser negativo.\n")
            return

        cantidad = int(input("Cantidad a agregar: "))
        if cantidad < 0:
            print("✗ El stock no puede ser negativo.\n")
            return
    except ValueError:
        print("✗ Entrada inválida.\n")
        return

    nuevo_id = obtener_id_unico()
    nuevo = {
        "id": nuevo_id,
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "stock": cantidad
    }

    celulares.append(nuevo)
    guardar_automaticamente(archivo_global)
    print(f"✓ Celular agregado correctamente con ID {nuevo_id}.")
    print(f"✓ Cambios guardados automáticamente en '{archivo_global}'.\n")

def cambiar_precio():
    if not celulares:
        print("✗ No hay celulares cargados.\n")
        return
    
    print()
    marca = input("Ingrese la marca a modificar precio: ").strip()
    encontrados = [cel for cel in celulares if cel["marca"].lower() == marca.lower()]

    if not encontrados:
        print("✗ No se encontró la marca.\n")
        return

    print("\n✓ Modelos encontrados:")
    for cel in encontrados:
        print(f"  ID: {cel['id']} - Modelo: {cel['modelo']} - Precio actual: ${cel['precio']:.2f}")

    try:
        nuevo_precio = float(input("\nNuevo precio para todos estos modelos: $"))
        if nuevo_precio < 0:
            print("✗ El precio no puede ser negativo.\n")
            return
        
        for cel in encontrados:
            cel["precio"] = nuevo_precio
        
        guardar_automaticamente(archivo_global)
        print(f"✓ Precio actualizado para {len(encontrados)} modelo(s).")
        print(f"✓ Cambios guardados automáticamente en '{archivo_global}'.\n")
    except ValueError:
        print("✗ Entrada inválida.\n")

def cambiar_stock():
    if not celulares:
        print("✗ No hay celulares cargados.\n")
        return
    
    print()
    try:
        id_buscar = int(input("ID del celular: "))
    except ValueError:
        print("✗ Entrada inválida.\n")
        return

    for cel in celulares:
        if cel["id"] == id_buscar:
            print(f"✓ Celular encontrado: {cel['marca']} {cel['modelo']}")
            print(f"  Stock actual: {cel['stock']}\n")
            try:
                nuevo_stock = int(input("Nuevo stock: "))
                if nuevo_stock < 0:
                    print("✗ El stock no puede ser negativo.\n")
                    return
                cel["stock"] = nuevo_stock
                guardar_automaticamente(archivo_global)
                print("✓ Stock actualizado.")
                print(f"✓ Cambios guardados automáticamente en '{archivo_global}'.\n")
            except ValueError:
                print("✗ Entrada inválida.\n")
            return

    print("✗ No se encontró el ID.\n")

def buscar_por_marca():
    if not celulares:
        print("✗ No hay celulares cargados.\n")
        return
    
    print()
    marca = input("Marca a buscar: ").strip()
    encontrados = [cel for cel in celulares if cel["marca"].lower() == marca.lower()]

    if encontrados:
        print("\n" + "="*90)
        print(f"{'ID':<8} {'Marca':<15} {'Modelo':<25} {'Precio':<12} {'Stock':<8}")
        print("="*90)
        for cel in encontrados:
            print(f"{cel['id']:<8} {cel['marca']:<15} {cel['modelo']:<25} ${cel['precio']:<11.2f} {cel['stock']:<8}")
        print("="*90 + "\n")
    else:
        print("✗ No se encontraron celulares con esa marca.\n")

def vender():
    if not celulares:
        print("✗ No hay celulares cargados.\n")
        return
    
    print()
    marca = input("Marca del celular a vender: ").strip()
    modelo = input("Modelo del celular a vender: ").strip()

    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():
            print(f"\n✓ Celular encontrado: {cel['marca']} {cel['modelo']}")
            print(f"  Precio: ${cel['precio']:.2f}")
            print(f"  Stock disponible: {cel['stock']}\n")

            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("✗ Cantidad inválida.\n")
                    return
            except ValueError:
                print("✗ Entrada inválida.\n")
                return

            if cantidad > cel["stock"]:
                print(f"✗ No hay suficiente stock. Disponibles: {cel['stock']}\n")
                return

            total_venta = cantidad * cel["precio"]
            cel["stock"] -= cantidad
            guardar_automaticamente(archivo_global)
            print(f"✓ Venta realizada exitosamente.")
            print(f"  Cantidad: {cantidad}")
            print(f"  Total: ${total_venta:.2f}")
            print(f"  Stock restante: {cel['stock']}")
            print(f"✓ Cambios guardados automáticamente en '{archivo_global}'.\n")
            return

    print("✗ No se encontró ese celular.\n")

def guardar_informacion(nombre_archivo):
    """Guarda manualmente los cambios"""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for cel in celulares:
                linea = f"{cel['id']},{cel['marca']},{cel['modelo']},{cel['precio']},{cel['stock']}\n"
                archivo.write(linea)
        print(f"✓ Cambios guardados correctamente en '{nombre_archivo}'.\n")
    except Exception as e:
        print(f"✗ Error al guardar: {e}\n")

def menu():
    archivo = "celulares.txt"
    crear_archivo_inicial(archivo)

    while True:
        print("\n" + "="*45)
        print("   SISTEMA DE GESTIÓN DE CELULARES")
        print("="*45)
        print("1. Cargar información")
        print("2. Agregar stock")
        print("3. Cambiar precio")
        print("4. Cambiar stock")
        print("5. Buscar por marca")
        print("6. Vender")
        print("7. Listar celulares")
        print("8. Guardar cambios")
        print("9. Salir")
        print("="*45)
        opcion = input("Elija una opción (1-9): ").strip()

        if opcion == "1":
            cargar_informacion(archivo)
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            cambiar_precio()
        elif opcion == "4":
            cambiar_stock()
        elif opcion == "5":
            buscar_por_marca()
        elif opcion == "6":
            vender()
        elif opcion == "7":
            mostrar_celulares()
        elif opcion == "8":
            guardar_informacion(archivo)
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("✗ Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()