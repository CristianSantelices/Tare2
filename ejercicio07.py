"""Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
 pero no debe repetise ningún elemento en la nueva lista:"""


lista1 = "Hola mundo"
lista2 = "Mundo bueno"
lista3 = []

for i in lista1:
    if i in lista2 and not i in lista3:
        lista3.append( i)
        
print( "La lista resultante es:", lista3)
 
 