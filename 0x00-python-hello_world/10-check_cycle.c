#include "lists.h"
/**
 * check_cycle - check cycle in a linkedlist
 * @list: linked list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *f_temp;

	temp1 = list;
	f_temp = list;
	while (temp1 && f_temp && f_temp->next)
	{
		temp1 = temp1->next;
		f_temp = f_temp->next->next;
		if (temp1 == f_temp)
		{
			return (1);
		}
	}
	return (0);
}
