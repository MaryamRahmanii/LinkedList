from Linked_list import Node,LinkedList
from doublylinkedlist import Node,DoublyLinkedList

linked_list =DoublyLinkedList()

for i in range(10):
    linked_list.addback(i)

linked_list.shift(1)


linked_list.printforward()
