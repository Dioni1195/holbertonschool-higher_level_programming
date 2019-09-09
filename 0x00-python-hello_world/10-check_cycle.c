#include "lists.h"

/**
* check_cycle - Check a linked list
* @list: The list to verify
*
* Return: Nothing
* On error, nothing
*/
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	int check_list = 1;

	while (list)
	{
		if (list->next == NULL)
		{
			check_list = 0;
			break;
		}
		else if (list->next == aux)
			break;
		list = list->next;
	}
	return (check_list);
}

