# Связанные списки
# Односвязные списки

# class Node:
#     def __init__(self, elem):
#         self.__data = elem
#         self.__next = None
#
#     def get_data(self):
#         return self.__data
#
#     def get_next(self):
#         return self.__next
#
#     def set_data(self, new_data):
#         self.__data = new_data
#
#     def set_next(self, new_next):
#         self.__next = new_next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def list_print(self):
#         val = self.head
#         while val:
#             print(val.get_data(), end=' ')
#             val = val.get_next()
#         print()
#
#     def add(self, item):
#         tmp = Node(item)
#         tmp.set_next(self.head)
#         self.head = tmp
#
#     def append(self, item):
#         temp = Node(item)
#         if self.head == None:
#             self.head = temp
#             return
#         end = self.head
#         while end.get_next():
#             end = end.get_next()
#         end.set_next(temp)
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current is not None:
#             count = count + 1
#             current = current.get_next()
#         return count
#
#     def insert(self, position, item): # вставить элемент в указанную позцию
#         if position > self.size():
#             raise IndexError("Индекс выходит за пределы списка")
#         current = self.head
#         previous = None
#         pos = 0
#         if position == 0:
#             self.add(item)
#             return
#         new_node = Node(item)
#         while pos < position:
#             pos += 1
#             previous = current
#             current = current.get_next()
#         previous.set_next(new_node)
#         new_node.set_next(current)
#
#     def search(self, item):
#         current = self.head
#         found = False
#         while current is not None and not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 current = current.get_next()
#         return found
#
#     def pop(self, position=None): # удаление элемента в начале, если позиция при вызове функции не указана
#         ret = None
#         current = self.head
#         if position is None:
#             ret = current.get_data()
#             self.head = current.get_next()
#         elif position > self.size() - 1:
#             raise IndexError("Индекс выходит за пределы списка.")
#         else:
#             pos = 0
#             previous = None
#             while pos < position:
#                 previous = current
#                 current = current.get_next()
#                 pos = pos + 1
#                 ret = current.get_data()
#             previous.set_next(current.get_next())
#         print(ret)
#         return ret
#
#     def reverse(self):
#         p = self.head
#         self.head = None
#         while p is not None:
#             p0, p = p, p.get_next()
#             p0.set_next(self.head)
#             self.head = p0
#
#
# temp = LinkedList()
# temp.head = Node(10)
# # temp.list_print()
# temp.append(11)
# temp.append(12)
# temp.append(13)
# temp.append(14)
# temp.add(9)
# temp.append(15)
# # temp.list_print()
# # print("Длина связного списка -", temp.size())
# temp.insert(2, 0)
# temp.list_print()
# # print(temp.search(12))
# # temp.pop(1)
# # temp.list_print()
# temp.reverse()

################################
# Двухсвязные списки

# class Node:
#     def __init__(self, elem, nxt=None, prev=None):
#         self.data = elem
#         self.next = nxt
#         self.prev = prev
#
#
# class DoublyLinkedList:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail
#
#     def is_empty(self):
#         return self.head is None and self.tail is None
#
#     def add(self, elem):
#         '''Добавление элемента в начало списка'''
#         if self.head is None:
#             item = Node(elem)
#             self.head = item
#             self.tail = self.head
#         else:
#             item = Node(elem, self.head)
#             self.head.prev = item
#             self.head = self.head.prev
#
#     def append(self, elem):
#         '''Добавление элемента в конец списка'''
#         if self.tail is None:
#             item = Node(elem)
#             self.head = item
#             self.tail = self.head
#         else:
#             self.tail.next = Node(elem, prev=self.tail)
#             self.tail = self.tail.next
#
#     def pop(self):
#         '''Удаление из конца списка'''
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.tail = self.tail.prev
#         self.tail.next = None
#
#     def shift(self):
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.head = self.head.next
#         self.head.prev = None
#
#     def print(self):
#         val = self.head
#         print("Список ссылок:")
#         while val:
#             print(val.data)
#             val = val.next
#         print()
#
#
# links = [
#     'http://site.ru',
#     'http://site.ru/news',
#     'http://site.ru/contacts',
#     'http://site.ru/about'
# ]
#
# link = DoublyLinkedList()
# for name in links:
#     link.add(name)
#
# while True:
#     if not link.is_empty():
#         link.print()
#     else:
#         print()
#         print("Список ссылок пустой.")
#     print("1 - добавить элемент в начало списка")
#     print("2 - добавить элемент в конец списка")
#     print("3 - удалить элемент из конца списка")
#     print("4 - удалить элемент из начала списка")
#     print("5 - выйти")
#     operation = input('=> ')
#     if operation == "1":
#         a = input("Новая ссылка: ")
#         link.add(a)
#     elif operation == "2":
#         a = input("Новая ссылка: ")
#         link.append(a)
#     elif operation == "3":
#         link.pop()
#     elif operation == "4":
#         link.shift()
#     elif operation == "5":
#         print("Всего доброго!")
#         break

#################################

# LIFO стек

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return f"{self.stack}"
#
#     def is_empty(self):
#         return self.stack == []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         return self.stack.pop()
#
#     def size(self):
#         return len(self.stack)
#
#     def show(self):
#         return self.stack
#
# brackets = {
#     ")": "(",
#     ">": "<"
# }
#
# def balanced_brackets(text):
#     s = Stack()
#     for c in text:
#         if c in brackets.values():
#             s.push(c)
#         elif c in brackets:
#             if s.is_empty():
#                 return False
#             elif brackets[c] != s.pop():
#                 return False
#     return s.is_empty()
#
# print(balanced_brackets('(<x)>(())()'))
# print(balanced_brackets('<((<<hello>>))>'))

############################

# Очередь (FIFO - first in first out - первым пришел, первым ушел)


# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def push(self, item):
#         self.queue.append(item)
#
#     def pop(self):
#         if len(self.queue) == 0:
#             return None
#         return self.queue.pop()
#
#     def show(self):
#         return self.queue
#
# s = Queue()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.show())
# s.pop()
# print(s.show())

############################

# Бинарное дерево поиска (BST - binary search tree)
# left < node < right

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    # def findval(self, val):

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(12)
root.insert(3)
root.print_tree()













