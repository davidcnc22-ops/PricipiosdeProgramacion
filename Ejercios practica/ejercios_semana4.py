""" numero= 0

numero= int (input("ingrese el numero:" ))

if numero %2 == 0:
    print ("El numero es par")
else:
    print ("El numero es impar") """

""" #Ejercicio 2

n1=0
n2=0

n1= int(input("ingrese el primer número: "))
n2= int(input("ingrese el sugundo número: "))

if n1 > n2:
    print("El numero 1 es mayor que el numero 2")
elif n1 < n2:
    print ("El numero 2 es mayor que el numero 1")
elif n1 == n2:
    print ("Los numeros son iguales") """

"""
#Ejercio 3

 calificacion=0

calificacion= int (input("ingrese la calificación:" ))

if calificacion >=70:
    print("Has aprobado")
else:
    print ("Has reprobado") """

""" #Ejercio 4

edad=0

edad= int (input("ingrese la edad:"))

if edad == 0 or edad == 12:
    print("Es un niño")
elif edad == 13 and edad < 18:
    print("es un adolecente")
else:
    edad > 18 
    print ("Es un adulto") """

""" #Ejercio 5

compra =0
descuento= 0.10

compra= int(input("ingrese el precio del producto: "))

if compra > 100:
    print ("tiene un descuento del 10%")
    compra = compra - (compra * descuento)
    print (f"El precio de su producto con descuento es {compra}")

else:
    print (f"El precio de su producto es {compra}") """

""" #Ejercio 6

n1=0
n2=0

operaciones=  ("+, -, *. /")

operacion=input("ingrese la operacion que desea realizar (+, -, *, /): ")

n1= int (input("ingrese el primer número:"))
n2= int (input("ingrese el segundo número:"))


if operacion == "+":
    print ("El resultado de la suma es:", n1+n2)

elif operacion == "-":
    print ("El resultado de la resta es:", n1-n2)
elif operacion == "*":
    print ("El resultado de la multiplicación es:", n1*n2)
elif operacion == "/":
    if n2 ==0:
        print("No se puede dividir entre 0")
    else:
        print ("El resultado de la división es:", n1 /n2)
else:
    print ("Opecación no validad")
     """

""" #Ejercio 7

calificio=0

calificacion= int (input("ingrese la calificación:"))

if calificacion >=90:
    print ("La calificaci[on numerica es A")
elif calificacion >= 80 or calificacion== 89:
    print("La calificacion numerica es B")
elif calificacion >=70 or calificacion == 79:
    print ("La calificacion numerica es C")
elif calificacion >=60 or calificacion == 69:
    print ("La calificacion numerica es D")
elif calificacion == 0 or calificacion <60:
    print("La calificacion  numerica es H")
     """
""" 
#Ejercio 8

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
    print("El triangulo es escaleno") 
 """

""" # Ejercio 9


temperatura=0 

temperatura= int (input("ingrese la temperatura:"))

if temperatura  < 0:
    print ("frio extremo")
elif temperatura >=0 and temperatura <30:
    print ("clima templado")
elif temperatura >=30:
    print ("calor extremo")
 """

""" # Ejercio 10

numero:0

numero= int (input ("ingrese un numero:"))

if  numero < 0:
    print("El numero es negativo")
elif numero == 0:
    print ("El numero es igual a cero")
else:
    print ("El numero es positivo") """

""" #Ejercio 11

numero=0

numero= int (input("ingrese el numero: "))

if numero == 1:
    print ("Lunes")
elif numero == 2:
    print("Martes")
elif numero ==3:
    print ("Miercoles")
elif numero == 4:
    print ("jueves")
elif numero ==5:
    print ("Viernes")
elif numero == 6:
    print ("Sabado")
elif numero == 7:
    print ("Domingo")
else:
    print("ingrese un numero válido") """

"""
#Ejercio 12

 annio=0

annio= int (input("ingrese el año: "))

if annio % 4 ==0:
    print("anio bisiesto")
elif annio %100 !=0:
    print("anno no bisiesto")
elif annio % 400==0:
    print("anno bisiesto") """
""" 
#Ejercicio 13

salario=0
impuesto = 0

salario = int (input("ingrese el salario: "))

if salario < 1000:
    print("No paga impuestos")

elif salario >= 1000 or salario <=2000:
    impuesto = salario * 0.10
    salario = (salario - impuesto)
    print("El salario paga impuesto")
    print(f"El salario después del 10%  descuento: {salario}")

elif salario > 2000:
    impuesto = salario * 0.20
    salario = (salario - impuesto)
    print("El salario paga impuesto")
    print(f"El salario después del 20 % descuento: {salario}")


 """

