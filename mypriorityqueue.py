"""
Ejercicio 3
A partir de las estructuras definidas como:
class PriorityQueue:
class PriorityNode:
Crear un módulo de nombre mypriorityqueue.py que implemente una cola con prioridad.
Una cola con prioridad es un TAD similar a una cola en la que los elementos tienen
adicionalmente, una prioridad asignada. En una cola de prioridades un elemento con mayor
prioridad será encolado antes que un elemento de menor prioridad. Si dos elementos tienen
la misma prioridad, se desencolarán siguiendo el orden de cola.
"""
from linkedlist import LinkedList,insert,length,access,delete,search,add,update

class PriorityQueue:
 head=None
class PriorityNode:
 value=None
 nextNode=None
 priority=None

"""
enqueue_priority(Q,element,priority)
Descripción: Agrega un elemento a Q con la prioridad priority
(entero), siendo Q una estructura de tipo PriorityQueue
Entrada: La cola Q sobre la cual se quiere agregar el elemento
(PriorityQueue), el valor del elemento (element) a agregar y un
número que indica la prioridad.
Salida: Devuelve la posición donde se inserto el elemento.
"""
def enqueue_priority(Q,element,priority):
  newNode = PriorityNode()
  newNode.value = element
  newNode.priority = priority
  newNode.nextNode = Q.head
  Q.head = newNode

  return 0
 

"""
dequeue_priority(Q)
Descripción: extrae el primer elemento de la cola Q con la mayor
prioridad (un valor mayor del campo priority, indica una mayor
prioridad), siendo Q una estructura de tipo PriorityQueue
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la cola sobre el cual se quiere realizar la eliminación
(PriorityQueue)
Salida: Devuelve el elemento con mayor prioridad. Devuelve None
si la cola está vacía.
"""
def dequeue_priority(Q):
  if (Q.head == None):
    return None
  
  elif (Q.head.nextNode == None):
    elementReturn = Q.head.value
    Q.head = None
    return elementReturn

  else:
    currentNode = Q.head
    mayorPriority = currentNode.priority

    while currentNode.nextNode != None:
      currentNode =   currentNode.nextNode
      if currentNode.priority > mayorPriority:
        mayorPriority = currentNode.priority 
    

    elements = length(Q)
    for i in range(elements, 0, -1):
      contador = i
      currentNode = Q.head
      if (contador == 1):
        if (currentNode.priority == mayorPriority):
          element = currentNode.value
          Q.head = Q.head.nextNode
          return element
      else:
          while (contador != 2):
            currentNode = currentNode.nextNode
            contador = contador - 1
          if currentNode.nextNode.priority == mayorPriority:
            element = currentNode.nextNode.value
            currentNode.nextNode = currentNode.nextNode.nextNode
            return element  


# trozo de codigo incompleto para return dequeue(revisar y completar despues)
"""
returnElement = currentNode.value
    currentNode.nextNode = currentNode.nextNode.nextNode
    return returnElement
"""