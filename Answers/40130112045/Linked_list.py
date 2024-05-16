from doublylinkedlist import Node,DoublyLinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
     self.head = None

    def addfront(self, data):
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node



    def addback(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node


    def removefirst(self):
        if self.head is None:
            return "List is empty"
        self.head = self.head.next

    def removelast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next=None




    def search(self, data):
        index=0
        temp=self.head
        while temp.next is not None:
            if temp.data==data:
                print("index:",index)
            temp=temp.next
            index+=1
        print("not found")


    def clear(self):
        self.head = None


    def size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print("size:",count)

    def printforward(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    def printbackward(self):

            arr=list()
            temp = self.head
            while temp:
                arr.append(temp.data)
                temp = temp.next
            for i in reversed(arr):
                print(i,end=" ")


    # def reverse_recursive(self):
    #     if self.head is None or self.head.next is None:
    #         return self.head
    #
    #     newhead = self.head.reverse_recursive()
    #     self.head.next.next=self.head
    #     self.head.next=None
    #
    #     return newhead






    def reverse_none_recursive(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def convert_singly_to_doubly(self):
        doubly = DoublyLinkedList()
        current = self.head
        prev = None
        while current:
            new_node = Node(current.data)
            if prev is not None:
                prev.next = new_node
                new_node.prev = prev
            else:
                doubly.head=new_node

            prev = new_node
            current = current.next
        return doubly


