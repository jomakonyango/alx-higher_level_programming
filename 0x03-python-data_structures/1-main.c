#include "lists.h"
#include <stdio.h>

int main(void)
{
    int my_list[] = {1, 2, 3, 4, 5};
    int idx = 3;
    int len = sizeof(my_list) / sizeof(int);
    int result = element_at(my_list, idx, len);

    if (result == -1)
    {
        printf("Index out of range\n");
    }
    else
    {
        printf("Element at index %d is %d\n", idx, result);
    }

    return 0;
}
