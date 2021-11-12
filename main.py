
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        if self.head == None:
            self.head = item
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = item

    def print(self):
        val = self.head
        while val.next != 

temp = LinkedList()
temp.append(1)

