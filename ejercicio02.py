"""
Realiza un programa que lea un número impar por teclado. 
Si el usuario no introduce un número impar,
debe repetise el proceso hasta que lo introduzca correctamente.
"""

def impar():
    n = int(input("Ingresa un numero impar: "))
    
    while n % 2 == 0:
        n = int(input("No es impar.Ingrese de nuevo: "))
    else:
        print(" Es impar")
impar()






