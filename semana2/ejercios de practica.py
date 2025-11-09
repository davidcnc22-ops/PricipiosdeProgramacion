""" """ """ """ """ a=0
b=0

""" 

""" a=0
b=0

# Entrada de datos


a=int(input("Ingrese el primer numero: "))          
b=int(input("Ingrese el segundo numero: "))

# Operaciones


if b == 0:
    print("No se puede dividir entre 0")
elif b < 0:
    print("No se puede dividir entre un numero negativo")
else:
    print(a/b)  """

""" -----------------------------------------------------------------------------------------
a=2
b=9

        
""" """ print("no se puede dividir entreb 0 " if b <=0 else "el resultrasdo es" , a/b) """
""" """  """ """
""" numero=0

# Entrada de datos
numero=int(input("Ingrese un numero par: "))
# Operaciones   
print("El numero es par" if numero % 2 == 0 else "El numero es impar") """


""" n """ """umero=0 """ """

# Entrada de datos
numero=int(input("Ingrese un numero par: "))

# Operaciones
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")  """

""" 

n1=0
n2=0

# Entrada de datos
n1=int(input("ingrese el primer numero:"))
n2=int(input("ingrese el segundo numero:"))

# Operaciones
if  n1 > n2:
    print("El numero mayor es ")
elif n1 <  n1:
    print("El numero menor es ")
else:
    print("Los numeros son iguales") """


""" numero1=0
numero2=0

# Entrada de datos

numero1=int(input("ingrese el mprimer numero:"))
numero2=int (input("ingrese el segundo numero:" ))

# Operaciones

if numero1  > numero2:
    print("el numero es mayor")
elif numero1< numero2 :
    print("el numero es menor")
   """  
""" else: 
    print("lows numeros son iguales") """

""" calificacion=0

# Entrada de datos
calificacion=int(input("ingrese la calificacion:")) 

# Operaciones
if calificacion ==70:
    print("aprobado")
elif calificacion > 70:
    print("aprobado")
else:
    print("reprobado") """

""" edad=0
# Entrada de datos
edad=int(input("ingrese su edad:"))

# Operaciones
if edad >= 0 and  edad <= 12:
     print("es un niño")
elif edad >=13 and edad <= 17:
    print("es un adolecente")
elif edad >= 18:
    print ("es un adulto")
else:
    print("ingrse un numero valido")
"""  """
total_compra=0
descuent=10
# Entrada de datos
total_de_compra=int(input("ingrese el totalo de la compra:"))

# Operaciones
if total_de_compra > 100:
    print("tiene un descuento del 10%")

else:
    print("no tiene descuento") """
""" total_compra=0
descuent=10
# Entrada de datos
total_de_compra=int(input("ingrese el totalo de la compra:"))
try:
    # Operaciones
    print("tiene un descuento del 10%" if total_de_compra > 100 else "no tiene descuento")      
except:
    print("ingrese un numero valido") """
""" # Solicita el total de la compra al usuario
total_compra = float(input("Ingrese el total de la compra: $"))

# Verifica si aplica el descuento
if total_compra > 100:
    descuento = total_compra * 0.10
    precio_final = total_compra - descuento
else:
    precio_final = total_compra

# Muestra el resultado
print(f"El precio final después del descuento es: ${precio_final:.2f}") """
""" 
# Mensaje de agradecimiento """ """ """
""" compra=0
impuesto=0.10
# Solicita el total de la compra al usuario
compra = int(input("Ingrese el total de la compra: $"))   

# Verifica si aplica el descuento
if compra > 100:
    descuento = compra * 0.10
    precio_final = compra - descuento
else:
    precio_final = compra
print(f"El precio final después del descuento es: ${precio_final:.2f}")
print("Gracias por su compra!")
# Mensaje de agradecimiento """
 
""" "" numero1=0
numero2=0
operaciones=  ("+, -, *. /")
            
# Entrada de datos
numero1=int(input("ingrese primer numero:")) 
numero2=int(input("ingrese segundo numero:"))

# Operaciones
operacion=input("ingrese la operacion que desea realizar (+, -, *, /): ")

if operacion == "+":
    print("El resultado de la suma es: ", numero1 + numero2)    
elif operacion == "-":
    print("El resultado de la resta es: ", numero1 - numero2)
elif operacion == "*":
    print("El resultado de la multiplicacion es: ", numero1 * numero2)
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("El resultado de la division es: ", numero1 / numero2)
else:
    print("Operacion no valida")  """

""" alificacion=0

calificacion=int(input("ingrese la calificacion:"))

if calificacion> 90 and calificacion == 100:

    print("A")  
elif calificacion >= 80 and calificacion < 90:
    print("B")      

elif calificacion >= 70 and calificacion < 80:
    print("C")
elif calificacion >= 60 and calificacion < 70:
    print("D")
elif calificacion >= 0 and calificacion < 60:
    print("F")

else:
    print("ingrese una calificacion valida")



 """

""" lado1=0
lado2=0        
lado3=0

# Entrada de datos
lado1=int(input("ingrese el primer lado del triangulo:"))
lado2=int(input("ingrese el segundo lado del triangulo:"))
lado3=int(input("ingrese el tercer lado del triangulo:"))
# Operaciones
if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")     
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno") """

""" grados =0
# Entrada de datos 

# Entrada de datos
grados = int (input("ingrese los grados celcios:"))

# Operaciones
try:

    if grados < 0:
        print ("frio extremo")

    elif grados >=0 and grados <= 30:
        print ("clima templado")

    else:
         print ("calor intenso")
except:
    print("ingrese un numero valido")
 """
""" numero=0


# Entrada de datos

numero = int (input("ingrese numero:"))

# Operaciones

if numero >0:
    print ("numero positivo")
elif numero <0:
    print ("numero negativo")
else:
    print ("cero") """



""" numero_de_dia=0

# Entrada de datos

numero_de_dia =int (input("ingrese el numero de dia:"))

# Operaciones

if numero_de_dia ==1:
    print("lunes")
elif numero_de_dia ==2:
    print("martes")
elif numero_de_dia ==3:
    print("miercoles")
elif numero_de_dia ==4:
    print("jueves")
elif numero_de_dia ==5:
     print ("viernes")
elif numero_de_dia == 6:
    print ("sabado")
elif numero_de_dia == 7:
    print("domingo")
else:
    print ("ingrese un numero valido")
 """


""" anno=0


# Entrada de datos

anno =int(input("ingrese el año:"))


# Operaciones


if anno % 4 ==0:
    print("anio bisiesto")
elif anno %100 !=0:
    print("anno no bisiesto")
elif anno % 400==0:
    print("anno bisiesto")  """

""" acumulador=0
contador=0

while contador <10:
    acumulador += contador
    contador +=1
    print (acumulador)

for i in range (10):
    acumulador += contador
    print (acumulador) """

""" acumulador=0
contador=0

opcion= input("ingrese ingrese una opciomn (a/b):")

while opcion== "a":
    acumulador += contador
    print ("entra")
    opcion= input("ingrese ingrese una opciomn (a/b):")
print("sale") """

""" *********************

contador1=int(input("ingrese un numero cualquiera:"))
contador=0
while contador <= contador1:
    print("numero:", contador)
    contador +=1
****************** """

"""
solicitar las variables de 5 salarios al usuario un por uno, sumar toddos y retotnar la suma total


"""
""" suma_total = 0

for i in range (5):
    salario = int(input(f"ingresar salario {i+1}:")) 

    suma_total = suma_total + salario
print("la suma total de los salarios es:", suma_total)
 """
    
"""
ejercios

recibir una cadena de texto ingtresada por el usuario e imprimir al reves


"""

""" texto = input("ingrese un mensaje: ")
texto_inverso = ""

for i in range (1,len(texto)+1):
    texto_inverso += texto [-i]

print(texto_inverso)  """


""" usuario_de_entrada:0 


# Entrada de datos

usuario_de_entrada= int (input("ingrese el usuario:"))

# Operaciones

if usuario_de_entrada > 0:
    print("acceso  concedido")
elif usuario_de_entrada < 0:
    print ("acceso no concedido")
elif usuario_de_entrada ==0:
    print ("ingrese un numero valido") """

"""
solicitar al usuario un nuero de entrada
si el numero ingresado en mayor que 0, imprimir  acceso concedido
si el numero ingresado menor que 0, imprimir accesno no valido
Si el numero ingresado  igual a 0, imprimir ingrese un numero valido
si se ingresa un numero con decimail, imprimir ingrese un numero entero
si se ingresa una letra,  imprimir ingrse un numero entero positivo
Si se ingresa un caracter especial  inprimir ingre un numero en en tero positivo

"""

""" usuario_de_entrada=0
# Entrada de datos

try:
    usuario_de_entrada= int (input("ingrese el usuario:"))

    # Operaciones

    if usuario_de_entrada > 0:
        print("acceso  concedido")
    elif usuario_de_entrada < 0:
        print ("acceso no concedido")
    elif usuario_de_entrada ==0:
        print ("ingrese un numero valido")
except ValueError:
    print("ingrese un numero entero positivo")
except:
    print("ingrese un numero entero positivo")
 """
