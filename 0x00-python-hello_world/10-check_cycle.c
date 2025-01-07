#include "lists.h"

/**
 * check_cycle -> Checks if singly linked list has cycle in it
 * @list: structure of the list
 * Return: 1 if there is cycle and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
