#include "lists.h"
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
	len = i - 1;
	j = len;
	for (i = 0; i <= len; i++)
	{
		if (buff[i] != buff[j])
			return (0);
		j--;
	}
	return (1);
}







