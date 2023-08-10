#include "lists.h"

/**
 * insert_node - Function to insert a value into a singly-linked list that is sorted.
 * @head: Pointer to the head of the linked list.
 * @number: The value to be inserted.
 *
 * Returns: A pointer to the newly inserted node on success, otherwise returns 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
