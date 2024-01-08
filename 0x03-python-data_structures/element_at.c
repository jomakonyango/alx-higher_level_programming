#include "lists.h"

int element_at(int *my_list, int idx, int len)
{
    if (idx < 0 || idx >= len)
        return -1;
    return my_list[idx];
}
