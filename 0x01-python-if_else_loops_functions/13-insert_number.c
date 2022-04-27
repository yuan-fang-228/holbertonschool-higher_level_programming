#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to the head pointer
 * @number: the number to be inserted
 * Return: the address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL;
	listint_t *current = NULL;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(*newnode));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else
	{
		current = *head;
		while (current->next != NULL)
		{
			if (current->next->n < number)
			{
				current = current->next;
			}
			else
				break;
		}
			newnode->next = current->next;
			current->next = newnode;
	}
	return (newnode);
}
