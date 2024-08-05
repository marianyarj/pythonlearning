"""10
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******
"""
def procedimiento (lista_num):
    for i in lista_num:
       print (i * "*")
       
procedimiento([4, 9, 7])
print("\n")
procedimiento([1 , 3, 5])
