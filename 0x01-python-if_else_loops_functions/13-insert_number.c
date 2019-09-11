#include "lists.h"

/**
  * insert_node - Function to insert a node
  * @head: The pointer of the list
  * @number: The number to add
  *
  * Return: Pointer
  * On error, Null
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *newNode;

	if (!head)
		return NULL;
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	aux = *head;
	if (!aux || (aux != NULL && aux->n > number))
	{
		newNode->next = aux;
		return (*head = newNode);
	}
	while (aux)
	{
		if (aux->next->n > number)
		{
			newNode->next = aux->next;
			aux->next = newNode;
			break;
		}
		aux = aux->next;
	}
	return (*head);
}



