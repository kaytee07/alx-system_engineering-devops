#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_when - this is for when done creating the zombies.
 *
 * Return: 0
 */
int infinite_when(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - start the process to creates five zombie processes.
 * Return: 0
 */
int main(void)
{
int i, pid;

for (i = 0; i < 5; i++)
{
pid = fork();

if (pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
return (0);
}
}
infinite_when();
return (0);
}
