""" # Declaracion de variables
edad_de_la_abuela_de_Ana_Actual = 0
edad_del_abuelo_de_Ana = 25
anno_del_matrimonio = 0

# Entrada de datos

anno_del_matrimonio = int(input("Ingrese el año en que se casaron los abuelos de Ana: "))


# Operaciones
edad_de_la_abuela_de_Ana_Actual =  anno_del_matrimonio / ( edad_del_abuelo_de_Ana - 7 ) 

# Salida de datos
print(f"La edad de la abuela de Ana es: {edad_de_la_abuela_de_Ana_Actual}")
 """


""" Ejercicio 5 """
# Declaracion de variables
Ganancia_de_Hugo = 0.0
Ganancia_de_Paco = 0.0
Ganancia_de_Luis = 0.0
ganancia_total = 0.0
ganancia_por_limonada = 0.0
Precio_Limonada = 10
Costo_Produccion = 5.50
Limonadas_Vendidas = 0.0


# Entrada de datos

Limonadas_Vendidas = float(input("Ingrese la cantidad de limonadas vendidas: "))


# Operaciones

ganancia_por_limonada = Precio_Limonada - Costo_Produccion
ganancia_total = ganancia_por_limonada * Limonadas_Vendidas

Ganancia_de_Hugo = ganancia_total * 0.40
Ganancia_de_Paco = ganancia_total * 0.30
Ganancia_de_Luis = ganancia_total * 0.30

# Salida de datos

print(f"Ganancia de Hugo: {Ganancia_de_Hugo}")
print(f"Ganancia de Paco: {Ganancia_de_Paco}")
print(f"Ganancia de Luis: {Ganancia_de_Luis}")
print(f"Ganancia total: {ganancia_total}")
