#include"lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if the linked list has a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *runner, *crawler;

	if (list == NULL || list->next == NULL)
		return (0);
	runner = list;
	crawler = list;
	while (runner != NULL && runner->next != NULL)
	{
		crawler = crawler->next;
		runner = runner->next->next;
		if (runner == crawler)
			return (1);
	}
	return (0);
}
