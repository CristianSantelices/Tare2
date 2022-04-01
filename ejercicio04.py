"""
Realiza un programa 
que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética:
"""

s = 0
n = int(input("¿Cuántos números quieres calcular? ") )
for x in range(n):
    s += int(input("Ingresa un número: ") )
print("La media es", s/n)