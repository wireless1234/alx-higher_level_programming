#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if a linked list has a cycle
 * @list: pointer to head of list
 * Return: 1 on success 0 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (current == NULL)
		return (0);
	while (current)
	{
		if (current->next == NULL)
			return (0);
		current = current->next;
		if (current == list)
			break;
	}
	return (1);
}
