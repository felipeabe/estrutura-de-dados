
class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0


    def insert_fim(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return

        pointer=self.head
        while pointer.next is not None:
            pointer=pointer.next

        pointer.next=Node(data,None)

    def tamanho_lista(self):
        cont=1
        pointer=self.head
        while pointer.next is not None:
            cont += 1
            pointer=pointer.next

        return cont


    def insert_at(self, data,index):

        if index==0:
            node = Node(data, self.head)
            self.head = node
            return

        count=0
        pointer=self.head
        while pointer is not None:
            if count == index-1:
                node=Node(data,pointer.next)
                pointer.next=node
            pointer=pointer.next
            count+=1


    def remove(self, elem):
        if self.head==None:
            raise ValueError
        elif self.head.data==elem:
            self.head=self.head.next

        else:
            ancestor=self.head
            pointer=self.head.next
            while pointer is not None:
                if pointer.data==elem:
                    ancestor.next=pointer.next
                    pointer.next=None

                ancestor = pointer
                pointer=pointer.next

    def imprime(self):
        if self.head is None:
            print('Empty list')
        else:
            pivot=self.head
            while pivot is not None:
                print(pivot.data)
                pivot=pivot.next
