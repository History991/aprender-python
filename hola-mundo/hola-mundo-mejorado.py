#!/bin/python3
import math

def hola_mundo():
    print('Hola mundo')

def calcular_raiz_cuadrada(numero): # Funcion que calcula la raiz cuadrada y se define el parametro (numero)
    return math.sqrt(numero)    # Raiz cuadrada

def funcion_principal(longitud): # Funcion principal y se define el parametro (longitud)
    hola_mundo() # Llamada a la funcion hola_mundo
    print ([x * 2 for x in range(longitud)]) # se lista el rango de longitud y se multiplica por 2 y se almacena en la variable (longitud)
    while True:
        numero = float(input('Introduce un numero: ')) # Se pide un numero con input y se almacena en la variable numero
        res = calcular_raiz_cuadrada(numero) # Se llama a la funcion calcular_raiz_cuadrada y se almacena en la variable (res)
        print(f'la raiz cuadrada de {numero} es {res}') # Se imprime el resultado

if __name__ == '__main__': # Se ejecuta la funcion principal
    funcion_principal(10)   # Llamada a la funcion "funcion principal"
    