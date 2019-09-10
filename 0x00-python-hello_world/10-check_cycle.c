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
	listint_t *tmp1 = list, *tmp2 = list;
	int check_list = 0;

	if (!list)
		return (check_list = 0);
	while (tmp2 != NULL && tmp2->next != NULL)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (check_list = 1);
	}
	return (check_list);
}

