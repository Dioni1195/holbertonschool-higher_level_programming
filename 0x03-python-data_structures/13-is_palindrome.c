#include "lists.h"
/**
 * is_palindrome - Verify if a list is palidrome
 * @head: pointer to list to be verified
 * Return: on success 1, o failure 0
 */
int is_palindrome(listint_t **head)
{
	int len, i = 0, ini, buff[1024];
	listint_t *aux = *head;

	if (!head || !*head || !aux->next)
		return (1);
	while (aux)
	{
		buff[i] = aux->n;
		i++;
		aux = aux->next;
	}
	len = i - 1;
	for (ini = 0; i <= len; ini++)
	{
		if (buff[ini] != buff[len])
			return (0);
		len--;
	}
	return (1);
}







