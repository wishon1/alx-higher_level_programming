#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linkedList is a palindrome
 * @head: Double pointer to the head of a list
 * Return: 0 if not else 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_node;
	int elements_array[2900] = {0};
	int array_index = 0, reversed_index = 2999;

	if (head == NULL)
		return (1);

	current_node = *head;

	if (current_node == NULL || current_node->next == NULL)
		return (1);

	while (current_node != NULL)
	{
		elements_array[reversed_index] = current_node->n;
		array_index++;
		reversed_index--;
		current_node = current_node->next;
	}
	current_node = *head;
	reversed_index++;

	while (current_node != NULL)
	{
		if (current_node->n != elements_array[reversed_index])
			return (0);
		reversed_index++;
		current_node = current_node->next;
	}

	return (1);
}
