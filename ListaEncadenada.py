from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None #Lo único que necesitamos es saber cuál es el primer nodo de mi lista. Cuando inicializamos nuestra lista aún NO tiene nodos, por lo tanto mi head es NONE

    #HEAD = Juana
    #Juana -> Next Pablo
    #Pablo -> Next Pedro
    #Pedro -> Next Elena
    #Elena -> Next None
    #nuevoNodo = Elena

    #aux = Juana
    #Juana.next = Pablo

    #aux = Pablo
    #Pablo.next = Pedro

    #aux = Pedro
    #Pedro.next = None

    #Pedro.next = Elena
    def insertaNodo(self, nuevoNodo):
        #1.- Si mi head es vacía, entonces en nuevoNodo es el primero de la lista
        if self.head == None:
            self.head = nuevoNodo
        else:
            #2.- Recorro mi lista hasta que encuentre el último elemento de mi lista. Cómo sé cuál es? Es aquel que tiene como next None
            aux = self.head #aux es el nodo en el que me encuentro en este momento
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo

    #Función que me imprima la lista que yo tengo
    #HEAD = Juana
    #Juana -> Next Pablo
    #Pablo -> Next Pedro
    #Pedro -> Next Elena
    #Elena -> Next None

    #aux = Juana
    #IMPRIMO Juana
    #aux = Juana.next = Pablo

    #IMPRIMO Pablo
    #aux = Pablo.next = Pedro

    #IMPRIMO Pedro
    #aux = Pedro.next = Elena

    #IMPRIMO Elena
    #aux = Elena.next = None
    def imprimeLista(self):
        aux = self.head #Comenzamos con el primer elemento
        while aux != None:
            print(aux.nombre)
            aux = aux.next

    #Función que elimine un nodo en base a su id
    #HEAD = Juana
    #Juana 1 -> Next Pablo
    #Pablo 2 -> Next Pedro
    #Pedro 3 -> Next Elena
    #Elena 4 -> Next None
    #id = 1
    #aux = Juana
    #Juana.id = 1 ? 
    #HEAD = Juana.next = Pablo
    #Juana.next = None
    def eliminaNodo(self, id):
        if self.head == None: #Si el head es none, mi lista está vacía
            print("Lista vacía, no podemos eliminar nodos")
        else:
            aux = self.head
            if aux.id == id:
                #1.- El nuevo head debe ser el next de mi nodo actual
                self.head = aux.next
                #2.- El nodo que quiero eliminar, ahora el NEXT es None, porque ya no lo queremos ligar a ninguna lista
                aux.next = None
            else:
                #HEAD = Juana
                #Juana 1 -> Next Pablo
                #Pablo 2 -> Next Pedro
                #Pedro 3 -> Next Elena
                #Elena 4 -> Next None

                #aux = Juana
                #prevAux = Juana

                #Juana.next = Pablo != None
                #prevAux = Juana
                #aux = Pablo
                #Pablo.id == 3 ? 

                #Pablo.next = Pedro != None
                #prevAux = Pablo
                #aux = Pedro
                #Pedro.id == 3 
                #Pablo.next = Pedro.next = Elena
                #Pedro.next = None
                prevAux = aux
                while aux.next != None:
                    prevAux = aux
                    aux = aux.next
                    #1.- Buscar en el nodo actual si hay una coincidencia en el ID
                    if aux.id == id:
                        #2.- Un nodo antes del actual, quiero que su siguiente nodo sea el nodo siguiente del actual
                        prevAux.next = aux.next
                        #3.- Al nodo actual (el que voy a eliminar), le pongo como siguiente NONE
                        aux.next = None