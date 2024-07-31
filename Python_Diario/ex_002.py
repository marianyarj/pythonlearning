#https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
""" 2
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1, n2, n3):
    if (n1 == n2 == n3):
        return "Son números iguales."
    elif (n3 >= n2 and n3 >= n1):
        return n3
    elif(n2 >= n3 and n2 >= n1):
        return n2
    else:
        return n1

n1 = -25
n2 = 8 
n3 = 8
print(max_de_tres(n1,n2,n3))
print(max(n1,n2,n3))

n1 = 9
n2 = 8 
n3 = 10
print(max_de_tres(n1,n2,n3))
print(max(n1,n2,n3))

n1 = 7
n2 = 4 
n3 = 2
print(max_de_tres(n1,n2,n3))
print(max(n1,n2,n3))

n1 = 7
n2 = 7 
n3 = 7
print(max_de_tres(n1,n2,n3))
print(max(n1,n2,n3))