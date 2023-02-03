#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - check palindrome
 * @head: linked list
 * return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int count, i, j;
	int *list;

	temp = *head;
	count = 0;
	while(*head != NULL)
	{
		count = count + 1;
		*head = (*head)->next;
	}
	list = malloc(sizeof(int) * (count));
	if (list == NULL)
		return (0);
	i = 0;
	while(temp != NULL)
	{
		list[i] = (temp)->n;
		temp = (temp)->next;
		i++;
	}
	for (i = 0, j = count - 1; i <= count - 1; i++, j--)
	{
		if(list[i] != list[j])
		{
			free(list);
			return (0);
		}
	}
	free(list);
	return (1);
}
