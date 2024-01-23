#!/usr/bin/python3
"""
This is the "100-singly_linked_list" module.

The 100-singly_linked_list module defines the Node class and the SinglyLinkedList class.
"""

class Node:
    """
    This is the Node class.
    
    The Node class defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        This is the constructor method for the Node class.
        
        Args:
            data (int): The data of the node, must be an integer.
            next_node (Node): The next node in the linked list, defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This is a getter for data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This is a setter for data.
        
        Args:
            value (int): The data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This is a getter for next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This is a setter for next_node.
        
        Args:
            value (Node): The next node in the linked list.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.
    
    The SinglyLinkedList class defines a singly linked list.
    """
    def __init__(self):
        """
        This is the constructor method for the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        This is a public instance method that inserts a new Node into the correct sorted position in the list (increasing order).
        
        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        This is a method that returns a string representation of the SinglyLinkedList.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

