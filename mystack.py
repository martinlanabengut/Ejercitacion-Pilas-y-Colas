"""
Ejercicio 1
Crear un módulo de nombre mystack.py que implemente las siguientes especificaciones de
las operaciones elementales para un TAD Pila utilizando el TAD Lista. Recordar que una
Pila puede implementarse también sobre una estructura LinkedList donde, el último
elemento en ingresar a la lista es el primero en salir (LIFO).
"""

from linkedlist import LinkedList,insert,length,access,delete,search,add,update

"""
push(S,element)
Descripción: Agrega un elemento al comienzo de S, siendo S una
estructura de tipo LinkedList
Entrada: La pila S sobre la cual se quiere agregar el elemento
(LinkedList) y el valor del elemento (element) a agregar.
Salida: No hay salida definida
"""

def push(S, element):
  add(S, element)
  return


"""
pop(S)
Descripción: extrae el primer elemento de la pila S, siendo S
una estructura de tipo LinkedList
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la pila S (Linkedlist) sobre el cual se quiere realizar
la eliminación
Salida: Devuelve el elemento eliminado. Devuelve None si la pila
está vacía.
"""
def pop(S):
  
  currentNode = S.head
  
  if (length(S) == 0):
    return None
  
  else:
    #accedo al elemento de la posicion 0
    deleteElement = access(S, 0)

    S.head = currentNode.nextNode

    return deleteElement


   

