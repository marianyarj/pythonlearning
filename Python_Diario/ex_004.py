""" 4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def is_vocal(caracter):
    vocales = "aàáâãeéiíoóôõuú"
    return caracter.lower() in vocales

print(is_vocal('a'))
print(is_vocal('é'))
print(is_vocal('z'))
print(is_vocal('Ú'))