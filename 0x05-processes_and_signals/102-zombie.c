#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

/**
 * infinite_while - a while loop that
 * runs infinitely and sleeps for 1
 * second in each iteration
 *
 * Return: 0
 *
 */


int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: 0 if successful
 *
 */

int main(void)
{
	int count = 0;
	pid_t child;

	for (count = 0; count < 5; count++)
	{
		child = fork();
		if (child > 0)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(EXIT_FAILURE);
	}

	infinite_while();

	return (0);
}

