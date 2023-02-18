#include <stdio.h>

void linear_sort(int *arr,int n,int *Cop)
{
	int i,j,min,temp;
	for(i=0;i<n;i++)
	{
		//min=i;
		for(j=i+1;j<n;j++)
		{
			++(*Cop);
			if(arr[j]<arr[i])
				{
					temp=arr[i];
					arr[i]=arr[j];
					arr[j]=temp;
				}
			//if(min==i)
			{
				
			}
		}
	}
}

void display(int arr[],int n)
{
	printf("array is:");
	for(int i=0;i<n;i++)
		printf("%d  ",arr[i]);
}

void main()
{
	int n,i,Cop=0;
	printf("enter size of array:");
	scanf("%d",&n);
	int arr[n];
	printf("enter elements: ");
	for(i=0;i<n;i++)
	{
		printf("arr[%d]=",i);
		scanf("%d",&arr[i]);
	}
	display(arr,n);
	linear_sort(&arr[0],n,&Cop);
	printf("\nafter sorting ");
	display(arr,n);
	printf("\noperation count is:%d",Cop);

}
