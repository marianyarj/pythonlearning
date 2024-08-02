""" 7
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ","")
    return cadena == cadena[::-1]

print(es_palindromo("Somos o no somos"))
print(es_palindromo("Luz azul"))
print(es_palindromo("mariazinha"))
print(es_palindromo("radar"))

