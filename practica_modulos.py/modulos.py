import math
print (math.sqrt(16))

import random

print (random.randint (10,16))

# escoje pieddra, papel o tijera
opciones = ["piedra", "papel", "tijera"]
eleccion = random.choice(opciones)
print("La elección aleatoria es:", eleccion)

# usa json 

import json

data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "San José"
}
json_string = json.dumps(data)
print("JSON string:", json_string)  
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)
print("Nombre:", parsed_data["nombre"])
print("Edad:", parsed_data["edad"])
print("Ciudad:", parsed_data["ciudad"])

# usa datetime
from datetime import datetime

fecha_actual = datetime.now()
print("Fecha y hora actual:", fecha_actual)
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateada:", fecha_formateada)
fecha_especifica = datetime(2023, 12, 25, 10, 30, 0)
print("Fecha específica:", fecha_especifica)
diferencia = fecha_especifica - fecha_actual
print("Días hasta la fecha específica:", diferencia.days)
# usa os
import os
directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)
nueva_carpeta = "nueva_carpeta_ejemplo"
os.makedirs(nueva_carpeta, exist_ok=True)   
print("Nueva carpeta creada:", nueva_carpeta)
os.rmdir(nueva_carpeta)
print("Carpeta eliminada:", nueva_carpeta)
# lista archivos en el directorio actual
archivos = os.listdir(directorio_actual)
print("Archivos en el directorio actual:", archivos)
# usa sys
import sys
print("Versión de Python:", sys.version)
print("Plataforma:", sys.platform)

print("Argumentos de línea de comandos:", sys.argv)
def mostrar_menu():
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

