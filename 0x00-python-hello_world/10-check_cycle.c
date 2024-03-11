#include "lists.h"

/**
 * check_cycle - check loop in LL
 * @a: head of linked list
 *
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *a)
{
	listint_t *slow, *fast;

	if (!a)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
