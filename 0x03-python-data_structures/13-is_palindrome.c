#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_palindrome - recursively check the given list is a palindrome or not
 * @head: a pointer pointed to the head pointer
 * @tail: a pointer to tail node
 * Return: 0 if not, 1 if yes
 */
int check_palindrome(listint_t **head, listint_t *tail)
{
	if (head != NULL && tail == NULL)
		return (1);
	if (check_palindrome(head, tail->next) == 0)
		return (0);
	if ((*head)->n != tail->n)
		return (0);
	*head = (*head)->next;
	return (1);
}
/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: a pointer pointed to the head pointer
 * Return: 0 if it is not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *tail = *head;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	return (check_palindrome(&start, tail));
}
