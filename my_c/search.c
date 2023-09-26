#include <stdio.h>
#include <string.h>
#define B_SIZE 1000


/**
* o_add - a function that add the found title that maches 
 * the pattern to a new list in an orderd maner
* Return: NULL
*
void sort(char **buff)
{
		
}
*/

void print_array(char *st[], size_t siz)
{
	int i;
	for (i = 0; st[i] != NULL; i++)
	{
		printf("%s\n", st[i]);
	}
}
/**
* searcher - a function that search for a perticular matching pattern
* data: the data to be sorted
* pattern: the pertern we are looking for while serching
* Return: NULL
*/
char **searcher(char **data, char *pattern, char *buf[])
{
	/*buff that sors pointer to the strings that match*/
	/* the int that helps to monitor the buff*/
	unsigned int b_i = 0;
	unsigned int i, j, k, flag = 0;
	size_t len;
	char *temp;
	
	buf[0] = NULL;
	len = strlen(pattern);
	if (data == NULL || pattern == NULL)
		return (NULL);
	for (i = 0; data[i] != NULL; i++)
	{
		temp = data[i];
		//printf("%d %s\n", 99, temp);
		for (j = 0; temp[j] != '\0'; j++)
		{
			flag = 0;
			//printf(" ++ %c\n", temp[j]);
			if (temp[j] == pattern[0])
			{
				//printf("--- %c - %d\n",temp[j], j);
				for (k = 0; k < len && temp[j] != '\0'; k++, j++)
				{
					//printf("*");
					if (pattern[k] == temp[j])
						flag += 1;
					else
					{
						//j - = 1;
						flag = 0;
						break;
					}
				}
				if (flag != len)
				{
					flag = 0;
					j -= 1;
				}
				//printf("%d %s\n", flag, temp);

			}
			/* if flag == len that means a match has been found */
			if (flag == len)
			{
				buf[b_i] =  temp;
				b_i += 1;
				if (b_i == B_SIZE)
					return (buf);
				buf[b_i] = NULL;
				//printf("%d %s\n", b_i, temp);
				//if (buf[b_i - 1] != NULL)
				//	printf("%s\n", buf[b_i - 1]);
				break;
			}

		}
	}
	return (buf);
}

int main()
{
	char *filter[B_SIZE];
	char *ar[] = {"adea", "aa", "aai", "caaa", "aaa", NULL};
	print_array(ar, 5);
	searcher(ar, "aa", filter);
	//if (filter[4] != NULL)
	//	printf("%s\n", filter[1]);
	print_array(filter, 5);
}
