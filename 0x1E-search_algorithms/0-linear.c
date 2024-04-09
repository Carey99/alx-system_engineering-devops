#include "search_algos.h"

/**
 * linear_search - Search for elements linearly
 * @array: Pointer to the first array to search
 * @size: Number of elements in array
 * @value: Value to search
 * Return: First index where the value is located
 */
int linear_search(int *array, size_t size, int value)
{
	size_t i;


	if (array == NULL || size == 0)
		return (-1);
	for (i = 0; i < size; i++)
	{
		printf("Value checked array[%ld] = [%d]\n", i, array[i]);
		if (array[i] == value)
		{
			return (i);
		}
	}
	return (-1);
}
