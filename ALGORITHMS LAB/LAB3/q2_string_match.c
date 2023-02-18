#include<stdio.h>
#include<string.h>
int naive_string_match(char str1[],char str2[],int *Cop)
{
	int i,j,ret=0;
	for(i=0;i<strlen(str1);i++)
	{
		if(str1[i]==str2[0])
			{
				++(*Cop);
				if(strlen(str1)-i<strlen(str2))
				{return 0;}
				for(j=0;j<strlen(str2);j++)
				{
					if(str1[i+j]!=str2[j]) //not matched
						break;
					else //everything is matched
						{return 1;}
				}

			}
	}
	return 0;
}

void main()
{
	int l1,l2,Cop=0;
	printf("enter lenth of main string:"); scanf("%d",&l1);
	char str1[l1];
	
	printf("enter main string:");
	scanf("%s",str1);

	printf("enter lenth of pattern string:"); scanf("%d",&l2);
	char str2[l2];
	printf("enter pattern string:");
	scanf("%s",str2);

	printf("main string:"); puts(str1);
	printf("pattern string:"); puts(str2);

	int res=naive_string_match(str1,str2,&Cop);
	if(res)
		printf("%s exists in %s",str2,str1);
	else
		printf("%s dosnt exist in %s",str2,str1);
	printf("\nCop=%d",Cop);
}
