#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
void print_python_list_info(PyObject *p);

/**
 * print_python_list_info -> prints some basic info about Python lists
 * @p: pyobject
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n");
    printf("[*] Size of Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}