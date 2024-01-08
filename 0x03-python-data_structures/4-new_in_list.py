#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    A function that replaces an element in a list at a specific position
    without modifying the original list.

    Args:
    my_list (list): The list of elements
    idx (int): The index of the element to replace
    element: The new element

    Returns:
    The modified list, or a copy of the original list if the index is out of range
    """
    # Create a copy of the list
    new_list = my_list.copy()
    
    # Replace the element at the specified index, if it is within range
    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element
    
    return new_list
