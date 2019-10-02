#!/usr/bin/python3
"""Contain a class Node that defines a node of a singly linked list
"""


class Node:
    """Class Node define a node of  a singly linked list
       Args:
        __size (int): The size of the square
        __position (tuple): Th position to print the matrix
       Attributes:
        __size (int): The size of the square
        __position (tuple): Th position to print the matrix

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property data, contains the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Property next node, property of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class square to make a matrix
       Args:
        __size (int): The size of the square
        __position (tuple): Th position to print the matrix
       Attributes:
        __size (int): The size of the square
        __position (tuple): Th position to print the matrix

    """
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        aux = self.__head
        new_node = Node(value)
        if self.__head is None:
            self.__head= new_node
            print(self.__head.data, self.__head.next_node, value, "vacio", new_node)
        elif self.__head.next_node is None:
            print("Primero")
            if value > self.__head.data:
                self.__head.next_node = new_node
            else:
                new_node.next_node = self.__head
                self.__head = new_node
            print(self.__head.data, self.__head.next_node.data)
        else:
            print("Siguiente")
            aux = self.__head
            while aux.next_node is not None:
                if value > aux.data:
                    new_node.next_node = aux.next_node
                    aux = new_node
                    print("Hola")
                    break
                aux = aux.next_node
            while self.__head.next_node is not None:
                print(self.__head.data)
                self.__head= self.__head.next_node
            print(self.__head.data , self.__head.next_node.data)



