#https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
""" 1
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max_n(n1, n2):
    if(n1>n2):
        return n1
    elif (n1<n2):
        return n2
    else:
        return "Números iguales."

n1 = -30
n2 = -32
print(max_n(n1,n2))
print(max(n1, n2))

n1 = 2
n2 = 2
print(max_n(n1,n2))
print(max(n1, n2))

n1 = 75
n2 = 150
print(max_n(n1,n2))
print(max(n1, n2))