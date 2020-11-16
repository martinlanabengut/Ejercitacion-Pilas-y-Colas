class LinkedList:
  head = None

class Node: 
  value = None
  nextNode = None

"""
add(L,element)
Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList
que representa el TAD secuencia.
Entrada: La Lista sobre la cual se quiere agregar el elemento
(LinkedList) y el valor del elemento (element) a agregar.
Salida: No hay salida definida
"""
def add(L, element):
  newNode = Node()
  newNode.value = element
  newNode.nextNode = L.head
  L.head = newNode
  return


"""
search(L,element)
Descripción: Busca un elemento de la lista que representa el TAD
secuencia.
Entrada: la lista sobre el cual se quiere realizar la búsqueda
(Linkedlist) y el valor del elemento (element) a buscar.
Salida: Devuelve la posición donde se encuentra la primera instancia
del elemento. Devuelve None si el elemento no se encuentra.
"""
def search(L, element):
  currentNode = L.head
  currentPosition = 0 

  while (currentNode != None):
    
    if (currentNode.value == element):
      return currentPosition  
    
    currentNode = currentNode.nextNode
    currentPosition += 1
  return None
  


"""
insert(L,element,position)
Descripción: Inserta un elemento en una posición determinada de la
lista que representa el TAD secuencia.
Entrada: la lista sobre el cual se quiere realizar la inserción
(Linkedlist) y el valor del elemento (element) a insertar y la
posición (position) donde se quiere insertar.
Salida: Si pudo insertar con éxito devuelve la posición donde se
inserta el elemento. En caso contrario devuelve None. Devuelve None si
la posición a insertar es mayor que el número de elementos en la
lista.
"""


def insert(L, element, position):

  currentPosition = 0
  currentNode = L.head 
  
  while (currentNode != None) and (currentPosition < position - 1):
    currentNode = currentNode.nextNode
    currentPosition += 1

  if (position == 0):
    add(L, element)
    return position
  
  elif (currentNode  != None):
    newNode = Node()
    newNode.value = element
    # dirigimos el puntero del nuevo nodo al nodo que será su predecesor.
    newNode.nextNode = currentNode.nextNode
    currentNode.nextNode = newNode
    
    return currentPosition+1
  else:
    return None

  

"""
delete(L,element)
Descripción: Elimina un elemento de la lista que representa el TAD
secuencia.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la lista sobre el cual se quiere realizar la eliminación
(Linkedlist) y el valor del elemento (element) a eliminar.
Salida: Devuelve la posición donde se encuentra el elemento a
eliminar. Devuelve None si el elemento a eliminar no se encuentra.
"""
def delete(L, element):
  # debo buscar en que posicion se encuentra el nodo con el elemento a eliminar
  position = search(L, element)
  currentNode = L.head

  if position == None:
    return None
  elif (position == 0):

    L.head = currentNode.nextNode
    return position
  else:
    currentPosition = 0

    while (currentNode != None) and (currentPosition < position-1):
      currentNode = currentNode.nextNode
      currentPosition += 1

     # una vez ubicado en el nodo anterior al nodo a eliminar, apunto el puntero del currentNode al nodo que se encuentra siguiente al nodo a eliminar. Ésta operación desvincula o elimina el nodo.
    currentNode.nextNode = currentNode.nextNode.nextNode

    return position    
    
    


"""
length(L)
Descripción: Calcula el número de elementos de la lista que representa
el TAD secuencia.
Entrada: La lista sobre la cual se quiere calcular el número de
elementos.
Salida: Devuelve el número de elementos.
"""
def length(L):

  currentNode = L.head
  listSize = 0 
  while (currentNode != None):
    currentNode = currentNode.nextNode
    listSize += 1

  return listSize

"""
access(L,position)
Descripción: Permite acceder a un elemento de la lista en una posición
determinada.
Entrada: La lista (LinkedList) y la position del elemento al cual se
quiere acceder.
Salida: Devuelve el valor de un elemento en una position de la lista,
devuelve None si no existe elemento para dicha posición.
"""
def access(L, position):
 
  currentNode = L.head
  currentPosition = 0 
 
  while (currentNode != None) and (position != currentPosition):
    currentNode = currentNode.nextNode
    currentPosition += 1
   
  if (position == currentPosition):
    return currentNode.value
  else:
    return None

    

    
    
"""
update(L,element,position)
Descripción: Permite cambiar el valor de un elemento de la lista en
una posición determinada
Entrada: La lista (LinkedList) y la position sobre la cual se quiere
asignar el valor de element.
Salida: Devuelve None si no existe elemento para dicha posición. Caso
contrario devuelve la posición donde pudo hacer el update.
"""

def update(L, element, position):

  currentNode = L.head
  currentPosition = 0

  while (currentNode != None) and (currentPosition != position):
    currentPosition += 1
    currentNode = currentNode.nextNode

  if (currentNode == None):
    return None
  else:
    currentNode.value = element
    return position





    
