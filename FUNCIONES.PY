#1.



def imprimir_edad (edad):
    if edad < 0:
        return print("Edad no disponible.")
    if edad <= 12:
        return print("Eres un niño. Juega y diviertete.")
    elif edad <= 17:
        return print("Eres un adolecente. Enfocate en tus estudios.")
    elif edad <= 64:
        return print("Eres un adulto. Ordena tu  vida.")
    else:
        return print("Eres un adulto mayor. Disfruta de tu hogar.")
        
edad = int(input("Ingrese su edad: "))
imprimir_edad(edad)
"""

"""
#2. 



def imprimir_tabla_de_multiplicar(numero, orientacion):
    if orientacion == 1:
        for i in range(1, 13):
            print(f"{numero} X {i} = {numero*i}")
    else:
        tabla = []
        for i in range(1, 13):
            tabla.append(f"{numero} X {i} = {numero*i}")
        print("  ".join(tabla))    
numero = int(input("Ingresa un numero: "))
if numero > 0:
    orientacion = int(input("1. Vertical.\n2. Horizontal.\n"))
    if orientacion == 1 or orientacion == 2:
        imprimir_tabla_de_multiplicar(numero, orientacion)
    else:
        print("Opcion incorrecta.")
else:
    print("Numero no valido.")
"""

"""
#3. 


import math
def es_primo(numero):
    if numero <= 1:
        return print(f"{numero} no es primo.")
    for i in range(2, int(math.sqrt(numero))+1):
        if numero%i == 0:
            return print(f"{numero} no es primo.")
    return print(f"{numero} es primo.")
numero = int(input("Ingresa un numero: "))
es_primo(numero)
"""

"""
#4. 

def imprimir_numeros_pares(limite):
    numeros_pares = []
    for i in range(1,limite + 1):
        numeros_pares.append(i*2)
    print(numeros_pares)
    sumar(numeros_pares)

def sumar(lista):
    return print(f"Sumatoria: {sum(lista)}")

imprimir_numeros_pares(6)
"""

"""
#5. 




def calcular_promedio(lista):
    return sum(lista)/len(lista)
def nota_mas_alta(lista):
    return max(lista)
def nota_mas_baja(lista):
    return min(lista)
def estudiantes_aprobados(lista):
    aprobados = 0
    for i in range(0, len(lista)):
        if lista[i] >= 3.0:
            aprobados += 1
    return aprobados
def convertir_str_a_lista(cadena):
    lista_calificaciones = []
    lista = cadena.split(",")
    for i in range(0, len(lista)):
        lista_calificaciones.append(float(lista[i].strip()))
    return lista_calificaciones
def main(lista):
    print(f"El promedio de la clase es: {calcular_promedio(lista)}\nLa nota más alta: {nota_mas_alta(lista)}\nLa nota mas baja: {nota_mas_baja(lista)}")
    print(f"Cantidad de estudiantes que aprobaron: {estudiantes_aprobados(lista)}")
calificaciones = input("Ingrese las calificaciones separadas por comas: ").strip()
main(convertir_str_a_lista(calificaciones))
"""

"""
#6.

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena
longitud = int(input("Ingresa la longitud de la contraseña: "))
if longitud < 4:
    print("Ingresa una longitud minimo de 4 caracteres.")
else:
    print(f"Contraseña generada: {generar_contrasena(longitud)}")  
""