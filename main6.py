# Связанные списки
class Node:
    def __init__(self, elem):
        self.__data = elem
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        val = self.head
        while val:
            print(val.get_data(), end=' ')
            val = val.get_next()
        print()

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            return
        end = self.head
        while end.get_next():
            end = end.get_next()
        end.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def insert(self, position, item): # вставить элемент в указанную позцию
        if position > self.size():
            raise IndexError("Индекс выходит за пределы списка")
        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
            return
        new_node = Node(item)
        while pos < position:
            pos += 1
            previous = current
            current = current.get_next()
        previous.set_next(new_node)
        new_node.set_next(current)


temp = LinkedList()
temp.head = Node(10)
# temp.list_print()
temp.append(11)
temp.append(12)
temp.append(13)
temp.append(14)
temp.add(9)
temp.append(15)
temp.list_print()
print("Длина связного списка -", temp.size())
temp.insert(2, 0)
temp.list_print()







