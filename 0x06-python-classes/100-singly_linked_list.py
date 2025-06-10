#!/usr/bin/python3
"""
A class Node that defines a node of a singly list by:
private and public instance attributes of data and next_node
"""

class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
        
    @property
    def next_node(self):
        return self.__next_node
        
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
            
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""
A class SinglyLinkedList that defines a singly linked list by:
private intance attribute head
"""


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self, head=None):
        self.__head = head
    
    def sorted_insert(self, value):
        """Inserts a new Node into the list in sorted order(ascending)"""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the list for printing"""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
