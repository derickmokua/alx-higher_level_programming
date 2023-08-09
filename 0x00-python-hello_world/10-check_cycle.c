#include "lists.h"

/**
 * check_cycle - Let's see if there's a sneaky cycle hiding in this singly linked list.
 * @list: Pointer to the starting node of the list.
 * Return: 0 if there's no cycle, 1 if a cycle is lurking.
 */

int check_cycle(listint_t *list)
{
  listint_t *current, *check;

  if (list == NULL || list->next == NULL)
    return (0);
  current = list;
  check = current->next;

  while (current != NULL && check->next != NULL
	 && check->next->next != NULL)
    {
      if (current == check)
	return (1);
      current = current->next;
      check = check->next->next;
    }
  return (0);
}
