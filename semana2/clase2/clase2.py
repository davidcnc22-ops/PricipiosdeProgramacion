"""" 

Este es mi primer programa en python
El programa debe solicitar al usuario 3 numeros enteros para la operacion
Autor: David Cordero
Fecha 9/11/2025

"""
 # ***************************variables***************************************
numero1=0  #Esto es una variable que almacena el valor del primer numero
numero2=0  #Esto es una variable que almacena el valor del segumdo  numero
numero3=0  #Esto es una variable que almacena el valor del tercer numero

resultadoSuma =0 #Esto es una variable que almacena el valor de la suma de los 3 valores
resultadoMultiplicion=0 # #Esto es una variable que almacena el valor de la multiplicacion de los 3 valores 

""""
Entrada de datos:
Se utilica la funcion imput()

Ejemplo: 
numero1 (init(input"ingrese el primer numero:")) 
numero2 (init(input"ingrese el segundo numero:")) 
nuemero3 (init(input"ingrese el tercer numero:")) 

Para salida de datos:
Se utiliza la funcion print()
"""

# *******************************Entrada de datos***********************************************
numero1= int(input("ingrese el primer numero"))
numero2= int(input ("ingrese el segundo numero"))
numero3= int(input ("ingrese el tercer numero"))

#*****************************************Procedimiento de Datos************************************
resultadoSuma= numero1 + numero2+ numero3 

resultadoMultiplicion= numero1 * numero2 * numero3 

print ("El resaultado de la suma es: ")
print (resultadoSuma)
print ("El resultado de la multiplicacion es: ")
print (resultadoMultiplicion)




















