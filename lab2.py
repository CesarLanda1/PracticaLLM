'''EJERCICIO 1'''

'''LISTAS'''
lista = [1,"Claudio",2,True,False,3]
print(lista)

print(lista.index(3))
print(lista[0:3])

lista.append(10)
lista.remove(2)
print(lista)

'''DICCIONARIOS'''
diccionario = {"Nombre": "Claudio", "Edad":24, "Distrito":"La Victoria"}
print(diccionario)

print(diccionario["Edad"])

diccionario["DNI"] = 70076739
print(diccionario)

'''EJERCICIO 2: FUNCIONES'''
'''Funcion 1'''
def suma (num1,num2):
    return num1 + num2

resultado = suma(5,6)
print(resultado)

'''Funcion 2'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
resultado = factorial(3)
print(resultado)


'''Funcion 3'''
def valor_max(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

listanum = [11,23,2,45,3]
maximo = valor_max(listanum)
print(maximo)  # Esto imprimirá 8

'''EJERCICIO 3: COMPRENSIÓN DE LISTAS'''
'''Ejercicio 1'''
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

'''Ejercicio 2'''
listacadenas = ["rojo","azul","verde","amarillo"]
vocales = 'aeiouAEIOU'
cadenas_con_vocal = [cadena for cadena in listacadenas if cadena[0] in vocales]
print(cadenas_con_vocal)

'''EJERCICIO 4: LAMBA'''
'''Ejercicio 1'''
fun1 = lambda x: x*x
resultado = fun1(3)
print(resultado)

'''Ejercicio 2'''
listanumeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, listanumeros))
print(duplicados)

'''EJERCICIO 5: MAP-REDUCE- FILTER'''
'''Ejercicio 1'''
temp_celcius = [8, 20, 30, 25, 40]
convertir = lambda celsius: (celsius * 9/5) + 32
temp_fahrenheit = list(map(convertir, temp_celcius))
print(temp_fahrenheit)

'''Ejercicio 2'''
from functools import reduce
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)

'''Ejercicio 3'''
numeros2 = [1, 2, 3, 4]
pares = list(filter(lambda x: x%2 == 0,numeros2))
print(pares)