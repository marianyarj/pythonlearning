""" 6
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    cadena_inversa = ""
    # range(len(cadena) - 1, -1, -1) -> start, stop, step: começa no último índice de 'cadena' (len(cadena) - 1), vai até o índice -1 (não incluído), e decrementa de -1 em -1
    for c in range(len(cadena)-1, -1, -1):
        cadena_inversa += cadena[c]
    return cadena_inversa

print(inversa("estoy probando"))