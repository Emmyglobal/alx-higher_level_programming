#include "lists.h"
#include <stdio.h>

/**
 * int check_cycle - checks if a singly linked lists has a cycle
 * @listint_t: structure
 * @list: linked list
 * Return: 0 if fail and 1 if successful
 */

int check_cycle(listint_t *list)
{
	listint_t* slow = list;
	listint_t* fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
