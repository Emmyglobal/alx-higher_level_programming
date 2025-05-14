#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node -> Inserts a number into a sorted singly list
 * Description: A number is inserted into a sorted list
 * @head: The firs node
 * @number: number to be inserted
 * Return: Address of new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp, *newP;
    int key;

    newP = malloc(sizeof(listint_t));
    if (newP == NULL)
        return (NULL);
    newP->n = number;
    newP->next = NULL;

    key = number;
    if(*head == NULL || key < (*head)->n)
    {
        newP->next = *head;
        *head = newP;
    }
    else{
        temp = *head;
        while(temp->next != NULL && temp->next->n < key)
        {
            temp = temp->next;
        }
        newP->next = temp->next;
        temp->next = newP;
    }
    return *head;
}
