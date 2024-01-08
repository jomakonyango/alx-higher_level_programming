#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that retrieves an element from a list.

    Args:
    my_list (list): The list of elements
    idx (int): The index of the element to retrieve

    Returns:
    The element at the specified index, or None if the index is out of range
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
