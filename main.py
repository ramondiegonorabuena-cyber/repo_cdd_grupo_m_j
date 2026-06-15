
########## Tipos de datos ##########

# Enteros
entero = 10

# Flotantes
flotante = 3.14

# Cadenas de texto
cadena = "Hola, mundo!"

# booleanos
booleano = True
booleano2 = False

# Listas
lista = [ 1, 2, 3, 4, 5 ]  #mutable

# Tuplas
tupla = ( 1, 2, 3, 4, 5 )  #inmutable

# Diccionarios
diccionario = { "nombre": "Juan", "edad": 30, "ciudad": "Madrid" }  # llave-valor

# Conjuntos
conjunto = { 1, 2, 3, 4, 5 }  # No permite elementos duplicados y no tiene un orden específico

print(entero)
print(flotante)
print(cadena)
print(booleano)
print(booleano2)
print(lista)
print(tupla)
print(diccionario)
print(conjunto)

def resta(a,b):
    return a - b
print(resta(10,5))