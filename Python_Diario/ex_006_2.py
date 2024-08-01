""" 6
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    #cadena[::-1] -> start, stop, step que neste exemplo está omitido
    cadena_inversa = cadena[::-1]
    return cadena_inversa



print(inversa("estoy probando"))