# # linked_list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         return self.head is None
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def delete(self, data):
#         if self.head is None:
#             print("List is empty. Cant delete.")
#             return
#
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#
#         current = self.head
#         while current.next:
#             if current.next.data == data:
#                 current.next = current.next.next
#                 return
#             current = current.next
#
#         print("error")
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
#
# a = LinkedList()
# print(a.is_empty())
# a.append(1)
# a.append(2)
# a.display()
# a.append(1)
# a.display()
# a.append(3)
# a.display()
# a.prepend(2)
# a.append(1)
# a.prepend(2)
# a.prepend(5)
# a.prepend(7)
# a.display()
# a.delete(1)
# a.display()
# print(a.is_empty())
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            print("the list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("error")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


a = LinkedList()
