#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print("Original list:", my_list)
    my_list.print_sorted()
    print("After sorting:", my_list)
