#!/usr/bin/python3
"""A class that defines a node for a singly linked list"""


class Node:
    """Node class and its fields and methods"""
    def __init__(self, data, next_node=None):
        """Node class initialized with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""A class that defines the singly linked list data structure"""


class SinglyLinkedList():
    """SinglyLinkedList class and its fields and methods"""
    def __init__(self):
        """SinglyLinkedList class initialized"""
        self.head_ptr = None
        self.tail = None
        self.length = 0

    def head(self):
        pass

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head_ptr is None:
            self.head_ptr = new_node
            self.tail = new_node
        else:
            temp = self.head_ptr
            while temp.next_node or self.length == 1:
                trail = temp
                temp = temp.next_node
                if temp and value > trail.data and value > temp.data:
                    continue
                elif value > trail.data:
                    trail.next_node = new_node
                    new_node.next_node = temp
                    return
                else:
                    new_node.next_node = trail
                    self.head_ptr = new_node
                    return
            temp.next_node = new_node
        self.length += 1

    def __str__(self):
        temp = self.head_ptr
        c = ''
        if not temp:
            return c

        while temp.next_node:
            c += f'{temp.data}\n'
            temp = temp.next_node
        c += f'{temp.data}'
        return c
