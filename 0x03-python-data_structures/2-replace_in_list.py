#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    A function that replaces an element of a list at a specific position.

    Args:
    my_list (list): The list of elements
    idx (int): The index of the element to replace
    element: The new element

    Returns:
    The modified list, or the original list if the index is out of range
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
