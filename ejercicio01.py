"""1) Realiza un programa que lea dos números por teclado
 y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""


nu1= int(input("Ingresa un numero: "))
nu2= int(input("Ingresa otro numero: "))
s = nu1+nu2
r = nu1-nu2
m = nu1*nu2
k = int(input("¿Que operacion quieres? \n 1 para sumar \n 2 para restar \n 3 para multiplicar \n Escoge un numero de la operacion que desees hacer: "))

if k == 1:
    print("La suma es", s)
elif k == 2:
    print("La resta es" , r)
elif k == 3:
    print("La resta es" , m)
else:
    print("Ingresa los numero asignados")

 














