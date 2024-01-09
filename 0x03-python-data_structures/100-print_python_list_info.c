#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A pointer to a Python object.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t alloc;
    Py_ssize_t i;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        PyObject *item;

        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
