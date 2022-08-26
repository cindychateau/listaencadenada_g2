from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada() #Comienzo mi lista VACIA

persona1 = Nodo("Juana", 1) #Comenzamos nuestros nodos con next vacio
persona2 = Nodo("Elena", 2)
persona3 = Nodo("Pedro", 3)
persona4 = Nodo("Pablo", 4)

#Función que me agregue un nodo a la lista
listaPersonas.insertaNodo(persona1) #Juana es el head
listaPersonas.insertaNodo(persona2) #Juana.next = Elena; Elena.next = None
listaPersonas.insertaNodo(persona3) #Juana.next = Elena; Elena.next = Pedro; Pedro.next = None
listaPersonas.insertaNodo(persona4) #Juana.next = Elena; Elena.next = Pedro; Pedro.next= Pablo; Pablo.next = None

listaPersonas.imprimeLista()