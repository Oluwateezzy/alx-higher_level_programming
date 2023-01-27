#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert number into a sorted linked list
 * @head: head of linked list
 * @number: number to be inserted
 * Return: llinked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (temp->next != NULL && temp->next->n < number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (temp);
}
