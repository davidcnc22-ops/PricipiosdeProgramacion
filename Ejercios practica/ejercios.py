""" producto=0
impuesto= 13
precio =0

producto = input ("ingrese el nombre del producto:") 
precio = int(input("ingrese el valor del producto: "))

#calculo del impuesto
impuesto = (precio * impuesto) / 100

#calculo del precio final
precio_final = precio - impuesto
print(f"el precio final del producto {producto} es de: {precio_final} ")
 """

""" Kilometraje_inicial=0
kilometraje_final=0
distancia_recorrida=0

kilometraje_incial= int (input("ingrese el kilometraje inical:"))
kilometraje_final= int (input("ingrese el kilometraje final:"))


#calculo de la distancia recorrida
distancia_recorrida= kilometraje_final - kilometraje_incial
print(f"la distancia recorrida es de: {distancia_recorrida} km") """

""" edad_ana=0
edad_elena=0

edad_elena= int (input("ingrese la edad:"))

edad_ana = edad_elena *2 + 10
print ("la edad de ana es: ", edad_ana)

"""  

""" edad_abuela_de_ana=0
edad_abuelo_de_ana=0
matrimonio=0

edad_abuelo_de_ana= int (input("ingresa la edad del abuelo de ana: "))
matrimanio= int (input("ingrese el año del matrimanio:"))

edad_abuela_de_ana = edad_abuelo_de_ana - 7 
print("La edad de la abuela de ana es:", edad_abuela_de_ana ) """


""" cantidad_de_limonadas=0
precio_por_limonada=10
costo_de_produccion=5.0
ganancia_total=0

cantidad_de_limonadas= int (input("ingrese la cantidad de limonadas vendidas: "))

#calculo de la ganancia total
ganancia_total= (precio_por_limonada - costo_de_produccion) * cantidad_de_limonadas



ganancia_de_hugo= ganancia_total * 0.40
ganancia_de_paco= ganancia_total * 0.30 
ganancia_de_luis= ganancia_total * 0.30
print(f"La ganancia total es de: {ganancia_total} ")
print(f"La ganancia de hugo es de: {ganancia_de_hugo} ")    
print(f"La ganancia de paco es de: {ganancia_de_paco} ")
print(f"La ganancia de luis es de: {ganancia_de_luis} ") """

""" salario_bruto=0
impuesto=0
salario_neto=0

salario_bruto= int (input("ingrese el salrio bruto: "))
impuesto= int (input("ingrese el impuesto: ")

salario_neto= salario_bruto - (impuesto  / 100 * salario_bruto)

print(f"el salario neto es de: {salario_neto} ")
 """

""" nombre_del_pais=""
cantidad_enfermos=0
Cantidad_muertos=0 
mortalidad=0

nombre_del_pais= (input("ingrese el nombre del país: "))
cantidad_enfermos = int(input("ingrese la cantidad de enfermos: "))
Cantidad_muertos= int (input("ingrese la cantidad de muertos: "))

mortalidad= (Cantidad_muertos / cantidad_enfermos) * 100

print ("la mortalidad del a nivel país es:", mortalidad)
 """

""" costo_base=0
impuesto_ventas=30
ganacia_vendedor= 15

costo_base = int (input("ingrese el costo base: "))

impuesto_ventas= (costo_base * impuesto_ventas) / 100
ganacia_vendedor= (costo_base * ganacia_vendedor) / 100

Costo_final= costo_base + impuesto_ventas + ganacia_vendedor    

print(f"el costo final del producto es de: {Costo_final} ") """

"""
Vilma envía a Pedro a comprar pan, jamón, queso, tomate y lechuga para el almuerzo. Pedro gasta
en total 2700 colones. Él dice que: Pan 15 %, Tomate 35 %, Queso 25 %, Lechuga 10 %, y el Jamón lo
restante. Haga un programa que calcule el costo en colones de cada ingrediente
"""

""" costo_total=2700
pan= (costo_total * 15) / 100
tomate= (costo_total * 35) / 100
queso= (costo_total * 25) / 100
lechuga= (costo_total * 10) / 100
jamon= costo_total - (pan + tomate + queso + lechuga)
print(f"el costo del pan es de: {pan} ")
print(f"el costo del tomate es de: {tomate} ")
print(f"el costo del queso es de: {queso} ")
print(f"el costo de la lechuga es de: {lechuga} ")
print(f"el costo del jamón es de: {jamon} ") """

""" precio_tiquete=0
descuento=15

precio_tiquete= int (input("ingrese el precio del tiquete: "))
descuento= precio_tiquete * descuento/100

precio_final= precio_tiquete - descuento

print(f"el precio final del tiquete es de: {precio_final} ") """

""" tarifa=50
cantidad_de_paginas_vendidas= 0

cantidad_de_paginas_vendidas= int (input("ingrese la cantidad de paginas vendidas: "))

ingreso= cantidad_de_paginas_vendidas * tarifa

print(f"el ingreso total por las paginas vendidas es de: {ingreso} ") """

""" hora_entrada=0
hora_salida=0
precio_hora=0



hora_entrada= int (input("ingrese la hora de entrada:"))
hora_salida= int (input("ingrese la hora de salida:"))
precio_hora= int (input("ingrese  el precio por hora:"))

horas_trabajadas= hora_salida - hora_entrada
salario_ganado= horas_trabajadas * precio_hora


print (f"el salario ganado por día es {salario_ganado}: ") """






