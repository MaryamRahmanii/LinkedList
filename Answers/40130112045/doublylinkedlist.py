class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None



    def addfront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


    def addback(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last=self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def removefirst(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def removelast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = None

    def clear(self):
        self.head = None

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                print("index:", index)

            current = current.next
            index += 1
        index = -1
        if index == -1:
            print("not found")

    def size(self):
        count = 0
        temp = self.head
        while temp.next is not None:
            count += 1
            temp = temp.next
        print("size:", count)



    def printforward(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


    def printbackward(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.prev



    def reverse_non_recursive(self):
        current = self.head
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            if current.prev is None:
                self.head = current

            current = temp





    def shift(self,num):
        if num>0:
            if self.head is None or self.head.next is None:
                return
            last=self.head
            second_last=None
            while last.next is not None:
                second_last=last
                last=last.next

            second_last.next=None
            last.prev=None
            last.next=self.head
            self.head.prev=last
            self.head=last



        if num<0:
            num=abs(num)
            current = self.head
            count = 1
            while count < num and current is not None:
                current = current.next
                count += 1

            if current is None:
                return

            k_node = current
            while current.next is not None:
                current = current.next

            current.next = self.head
            self.head.prev=current
            self.head = k_node.next
            self.head.prev=None
            k_node.next = None
        if num==0:
            return