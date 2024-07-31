""" 3 
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def len_cadena(cadena):
    contador = 0
    for c in cadena:
        contador += 1
    return contador

frase = "Olá, meu povo!"
print(len_cadena(frase))
print(len(frase))

print(len_cadena(""))
print(len(""))