#include <stdio.h>
#include <string.h>
#define B_SIZE 1000


/* void sort(char **buff)*/
/*{*/
/*}*/

/**
* print_array - this function prints an array containing strings
 * provided that the array ends with NULL
* @st: array to be printe
* Return: NULL
*/
void print_array(char *st[])
{
	int i;

	for (i = 0; st[i] != NULL; i++)
	{
		printf("%s\n", st[i]);
	}
}



/**
* searcher - a function that search for a perticular matching pattern
* @data: the data to be sorted
* @pattern: the pertern we are looking for while serching
* @buf: buffer to store the matching value
* Return: NULL
*/
void searcher(char **data, char *pattern, char *buf[])
{
	unsigned int b_i = 0, i, j, k, flag;
	size_t len;
	char *temp;

	buf[0] = NULL;
	len = strlen(pattern);
	if (data == NULL || pattern == NULL)
		return;
	for (i = 0; data[i] != NULL; i++)
	{
		temp = data[i];
		for (j = 0; temp[j] != '\0'; j++)
		{
			flag = 0;
			if (temp[j] == pattern[0])
			{
				for (k = 0; k < len && temp[j] != '\0'; k++, j++)
				{
					if (pattern[k] == temp[j])
						flag += 1;
					else
					{
						flag = 0;
						break;
					}
				}
				if (flag != len)
				{
					j -= 1;
				}

			}
			/* if flag == len that means a match has been found */
			if (flag == len)
			{
				buf[b_i] =  temp;
				b_i += 1;
				if (b_i == B_SIZE)
					return;
				buf[b_i] = NULL;
				break;
			}

		}
	}
}


/**
* main - the main func
* Return: int 0
*/
int main(void)
{
	char *filter[B_SIZE];
	char *ar[] = {"adea", "aa", "aai", "caca", "aaacaaa", "egg",\
	       	"my name", "who are you", "ade", NULL};

	print_array(ar);
	searcher(ar, "e", filter);
	printf(".............................\n");
	print_array(filter);
	return (0);
}
