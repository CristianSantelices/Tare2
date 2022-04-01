""" Realiza un programa que pida al usuario un número entero del 0 al 9,
 y que mientras el número no sea correcto se repita el proceso.
  Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar
 fácilmente si un valor se encuentra en una lista (devuelve True o False)"""


n = int(input("Ingresa un numero no mayor a 9: "))
while n >= 9:
    t = int(input("Ingresa un numero no mayor a 9: "))
    if t >= 9:
        t = int(input("Ingresa un numero no mayor a 9: "))
    break
if n <= 9:
    print("Esta en el rango de 0 al 9")

   
