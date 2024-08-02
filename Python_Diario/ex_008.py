""" 8
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
def superposicion(lista_i, lista_ii):
    for i in lista_i:
        if (i in lista_ii):
            return True
    return False

print(superposicion([1, 2, 3, 4], [9, 8, 7, 6]))
print(superposicion([1, 2, 3, 4], [9, 8, 4, 6]))
print(superposicion([1, 2, 6, 4], [9, 8, 7, 6]))