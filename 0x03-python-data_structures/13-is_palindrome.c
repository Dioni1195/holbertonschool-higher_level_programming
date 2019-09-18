#include "lists.h"
/**
*  list_len- Calculate the lenght of a string
* @h: The list passed
*
* Return: An unsigned int that is the count of nodes
* On error, nothing
*/
size_t list_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
/**
 * is_palindrome - Verify if a list is palidrome
 * @head: pointer to list to be verified
 * Return: on success 1, o failure 0
 */
int is_palindrome(listint_t **head)
{
	int len, i = 0, j;
	char buff[1024];
	listint_t *aux;

	if (!head || !*head || !(*head)->next)
		return (1);
	aux = *head;
	while (aux)
	{
		buff[i] = (char)aux->n;
		i++;
		aux = aux->next;
	}
	len = (int)list_len(*head);
	j = len - 1;
	for (i = 0; i != len / 2; i++)
	{
		if (buff[i] != buff[j])
			return (0);
		j--;
	}
	return (1);
}







