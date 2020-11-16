"""
Ejercicio 2
Crear un módulo de nombre myqueue.py que implemente las siguientes especificaciones de
las operaciones elementales para un TAD Cola utilizando el TAD Lista. Recordar que una
Cola puede implementarse también sobre una estructura LinkedList donde, el primer
elemento en ingresar a la lista es el primero en salir (FIFO).
"""

from linkedlist import LinkedList,insert,length,access,delete,search,add,update


"""
enqueue(Q,element)
Descripción: Agrega un elemento al final de Q, siendo Q una
estructura de tipo LinkedList.
Entrada: La cola Q (LinkedList) sobre la cual se quiere agregar
el elemento y el valor del elemento (element) a agregar.
Salida: No hay salida definida.
"""
def enqueue(Q, element):
  add(Q, element)

  return
 
 

"""
dequeue(Q)
Descripción: extrae el primer elemento ingresado a la cola Q, siendo Q
una estructura de tipo LinkedList.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la cola Q (Linkedlist) sobre el cual se quiere realizar la eliminación.
Salida: Devuelve el elemento de la cola. Devuelve None si la
cola está vacía.
"""
def dequeue(Q):

  currentNode = Q.head

  if length(Q) == 0:
    return None
  
  elif (length(Q) == 1):
    
    deleteElement = access(Q, length(Q)-1)
    
    Q.head = currentNode.nextNode

    return  deleteElement
  
  else:
    deleteElement = access(Q, length(Q)-1)
    currentPosition = 0

    while (currentNode != None) and (currentPosition < length(Q)-2):
      currentNode = currentNode.nextNode
      currentPosition += 1

     # una vez ubicado en el nodo anterior al nodo a eliminar, apunto el puntero del currentNode al nodo que se encuentra siguiente al nodo a eliminar. Ésta operación desvincula o elimina el nodo.
    currentNode.nextNode = currentNode.nextNode.nextNode

    return deleteElement



    
    

    
