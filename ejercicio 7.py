#Implementar los algoritmos necesarios para resolver las siguientes tareas:
#a. concatenar dos listas, una atrás de la otra;
#b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

from lista import Lista
from random import randint

lista1 = Lista()
lista2 = Lista()
lista_concatenada = Lista()

cont_repetidos = 0

for i in range(5):
    lista1.insertar(randint(5,20)) #cargamos las dos listas
    lista2.insertar(randint(1,20))

lista1.barrido()
print()
lista2.barrido()
print()

#Punto B
for i in range(lista1.tamanio()):
    dato1 = lista1.obtener_elemento(i)
    lista_concatenada.insertar(dato1)

for i in range(lista2.tamanio()):
    dato2 = lista2.obtener_elemento(i)
    lista_concatenada.insertar(dato2)

print("Dos listas en una sola omitiendo los datos repetidos y manteniendo su orden")
lista_concatenada.barrido()
print()

#Punto C
for i in range(lista1.tamanio()):
	num = lista1.obtener_elemento(i)
	pos = lista2.busqueda(num)
	if (pos != -1):
		cont_repetidos += 1

print('la cantidad de elementos repetidos son: ', cont_repetidos)
print()

#Punto A
lista1.set_elementos(lista2.get_elementos())
print("Dos listas, una atrás de la otra")
lista1.barrido()
print()

#Punto D
for i in range(lista1.tamanio()):
    dato = lista1.obtener_elemento(i)
    print("dato a eliminar: ",dato)
lista1.eliminar(dato)
print()


