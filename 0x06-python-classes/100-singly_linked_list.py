#!/usr/bin/python3
"""Class Node"""
class Node:
    def __init__(self, data, next_node=None):
        """Constructor"""
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """data getter"""
        return self.__data

    @property
    def next_node(self):
        """node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """node setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @data.setter
    def data(self, value):
        """data setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


"""Class SinglyLinkedList"""
class SinglyLinkedList:
    def __init__(self):
        """constructor"""
        self.head = None

    def __str__(self):
        """String representaion"""
        current = self.head
        output = ""
        while current:
            if not current.next_node:
                output += str(current.data)
            else:
                output += str(current.data) + "\n"
            current = current.next_node
        return output
    
    def sorted_insert(self, value):
        """sorted list"""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
