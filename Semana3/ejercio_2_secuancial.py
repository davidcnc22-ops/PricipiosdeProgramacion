# Declaracion de variables
cantidad_noches = 0 
precio_x_noche= 100
descuento= 5
total_a_cobrar=0


# Entrada de datos
cantidad_noches = int(input("ingrese la cantidad de noches que se va a quedar:"))
                    
# Operaciones

total_a_cobrar = cantidad_noches * precio_x_noche * 1- (1- descuento/100)
print(f"Precio con descuento: {"precio_final"}")

# Salida de datos

print("total a cobrar es", total_a_cobrar)