""" 5 
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum_num(lista):
    resultado = 0
    for num in lista:
        resultado += num
    return resultado
def multi_num(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

print(sum_num([1,2,3,4]))
print(multi_num([1,2,3,4]))