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

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def pop(self, position=None): # удаление элемента в начале, если позиция при вызове функции не указана
        ret = None
        current = self.head
        if position is None:
            ret = current.get_data()
            self.head = current.get_next()
        elif position > self.size() - 1:
            raise IndexError("Индекс выходит за пределы списка.")
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.get_next()
                pos = pos + 1
                ret = current.get_data()
            previous.set_next(current.get_next())
        print(ret)
        return ret

    def reverse(self):
        p = self.head
        self.head = None
        while p is not None:
            p0, p = p, p.get_next()
            p0.set_next(self.head)
            self.head = p0

    def remove(self, value):
        amount = self.size()
        current = self.head
        if self.head is None:
            raise ValueError("Такого элемента в списке нет!")
        if current.get_data() == value:
            self.head = current.get_next()
            return 0
        for i in range(0, amount):
            if current.get_next().get_data() != value:
                current = current.get_next()
            else:
                current.set_next(current.get_next().get_next())
                return i + 1
        raise ValueError("Такого элемента нет в списке!")

    def index(self, value):
        amount = self.size()
        current = self.head
        if self.head is None:
            return ValueError("Такого элемента в списке нет!")
        for i in range(0, amount):
            if current.get_data() == value:
                return i
            else:
                current = current.get_next()
        return None


temp = LinkedList()
temp.head = Node(1)
temp.append(2)
temp.append(3)
temp.append(4)
temp.append(5)
temp.append(6)
temp.list_print()
temp.remove(4)
temp.list_print()
print(temp.index(6))


