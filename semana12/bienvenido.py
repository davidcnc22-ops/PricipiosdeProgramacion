
import random
import os

ARCHIVO = os.path.join(os.path.dirname(__file__), "celulares.txt")

# Lista de diccionarios que almacena los celulares en memoria
celulares = []
modificado = False  # Variable global para saber si hubo cambios

def cargar_informacion(nombre_archivo=ARCHIVO):
    global celulares, modificado
    celulares = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) != 5:
                    # línea malformada, saltar
                    continue
                try:
                    id_cel = int(partes[0])
                    marca = partes[1]
                    modelo = partes[2]
                    precio = float(partes[3])
                    stock = int(partes[4])
                except ValueError:
                    continue
                celulares.append({
                    "id": id_cel,
                    "marca": marca,
                    "modelo": modelo,
                    "precio": precio,
                    "stock": stock
                })
        modificado = False
        print("Información cargada correctamente.\n")
    except FileNotFoundError:
        # crear archivo vacío si no existe
        open(nombre_archivo, "a", encoding="utf-8").close()
        celulares = []
        modificado = False
        print("El archivo no existe. Se creará cuando se guarde.\n")


def guardar_informacion(nombre_archivo=ARCHIVO):
    global modificado
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for cel in celulares:
                archivo.write(f"{cel['id']},{cel['marca']},{cel['modelo']},{cel['precio']},{cel['stock']}\n")
        modificado = False
        print(f"Cambios guardados correctamente en '{os.path.basename(nombre_archivo)}'.\n")
    except Exception as e:
        print(f"Error al guardar: {e}\n")


def mostrar_celulares():
    if not celulares:
        print("No hay celulares cargados.\n")
        return
    for cel in celulares:
        print(cel)
    print()


def existe_celular(marca, modelo):
    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():
            return True
    return False


def generar_id_unico():
    ids = {cel["id"] for cel in celulares}
    while True:
        nuevo = random.randint(1, 5000)
        if nuevo not in ids:
            return nuevo


def agregar_stock():
    global modificado
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    if existe_celular(marca, modelo):
        print("Ya existe un celular con esa marca y modelo.\n")
        return

    try:
        precio = float(input("Precio: "))
        if precio < 0:
            print("El precio no puede ser negativo.\n")
            return

        cantidad = int(input("Cantidad a agregar: "))
        if cantidad < 0:
            print("El stock no puede ser negativo.\n")
            return
    except ValueError:
        print("Entrada inválida.\n")
        return

    nuevo = {
        "id": generar_id_unico(),
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "stock": cantidad
    }

    celulares.append(nuevo)
    modificado = True
    guardar_informacion(ARCHIVO)
    print("Celular agregado y guardado correctamente.\n")


def cambiar_precio():
    global modificado
    marca = input("Ingrese la marca a modificar precio: ").strip()

    encontrados = [cel for cel in celulares if cel["marca"].lower() == marca.lower()]
    if not encontrados:
        print("No se encontró la marca.\n")
        return

    print("Modelos encontrados:")
    for cel in encontrados:
        print(f"{cel['id']} - {cel['modelo']} - ${cel['precio']:.2f}")

    try:
        id_elegido = int(input("Ingrese el ID para cambiar precio (o 0 para aplicar a todos): "))
    except ValueError:
        print("Entrada inválida.\n")
        return

    if id_elegido == 0:
        try:
            nuevo_precio = float(input("Nuevo precio para todos los modelos de la marca: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.\n")
                return
        except ValueError:
            print("Entrada inválida.\n")
            return
        for cel in encontrados:
            cel["precio"] = nuevo_precio
        modificado = True
        guardar_informacion(ARCHIVO)
        print("Precios actualizados y guardados.\n")
        return

    for cel in encontrados:
        if cel["id"] == id_elegido:
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return
            cel["precio"] = nuevo_precio
            modificado = True
            guardar_informacion(ARCHIVO)
            print("Precio actualizado y guardado.\n")
            return

    print("ID no encontrado entre los modelos de esa marca.\n")


def cambiar_stock():
    global modificado
    try:
        id_buscar = int(input("ID del celular: "))
    except ValueError:
        print("Entrada inválida.\n")
        return

    for cel in celulares:
        if cel["id"] == id_buscar:
            try:
                nuevo_stock = int(input("Nuevo stock: "))
                if nuevo_stock < 0:
                    print("El stock no puede ser negativo.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return

            cel["stock"] = nuevo_stock
            modificado = True
            guardar_informacion(ARCHIVO)
            print("Stock actualizado y guardado.\n")
            return

    print("No se encontró el ID.\n")


def buscar_por_marca():
    marca = input("Marca a buscar: ").strip()
    encontrados = [cel for cel in celulares if cel["marca"].lower() == marca.lower()]

    if encontrados:
        for cel in encontrados:
            print(cel)
        print()
    else:
        print("No se encontraron celulares con esa marca.\n")


def vender():
    global modificado
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():

            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("Cantidad inválida.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return

            if cantidad > cel["stock"]:
                print("No hay suficiente stock.\n")
                return

            cel["stock"] -= cantidad
            modificado = True
            guardar_informacion(ARCHIVO)
            print("Venta realizada y guardada.\n")
            return

    print("No se encontró ese celular.\n")


# MENU PRINCIPAL
def menu():
    archivo = ARCHIVO
    cargar_informacion(archivo)

    while True:
        print("===== SISTEMA DE CELULARES =====")
        print("1. Cargar información")
        print("2. Agregar nuevo celular")
        print("3. Cambiar precio")
        print("4. Cambiar stock")
        print("5. Buscar por marca")
        print("6. Vender")
        print("7. Listar celulares")
        print("8. Guardar cambios")
        print("9. Salir")
        opcion = input("Elija una opción: ")

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
            if modificado:
                guardar = input("¿Desea guardarlos antes de salir? (s/n): ").lower()
                if guardar == "s":
                    guardar_informacion(archivo)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()