#include<stdio.h>
void bubble_sort(int *arr,int n,int *Cop)
{
	int i,j,min,temp;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			
			if(arr[j]>arr[j+1])
				{
					++(*Cop);
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
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
	bubble_sort(&arr[0],n,&Cop);
	printf("\nafter sorting ");
	display(arr,n);
	printf("\noperation count is:%d",Cop);
}
