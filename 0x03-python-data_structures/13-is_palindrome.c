#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp = NULL;
    listint_t *second_half;

    if (*head == NULL || (*head)->next == NULL)
        return 1;  /* Empty or one-element list is a palindrome */

    /* Reverse the first half while finding the middle*/
    while (fast && fast->next)
    {
        fast = fast->next->next;

        /* Reverse current slow node */
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* For odd-length list, skip the middle node*/
    if (fast)
        slow = slow->next;

    second_half = slow;

    /* Compare reversed first half (prev) with second half*/
    while (prev && second_half)
    {
        if (prev->n != second_half->n)
            return 0;
        prev = prev->next;
        second_half = second_half->next;
    }

    return 1;
