#include<stdio.h>
#include "mpi.h"
int main(int argc,char * argv[])
{
	int size,rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int n=5,chunk=1,fact=1,sum=0;
	int array[n],b;
	int factorials[n];
	if(rank==0)
	{
		printf("enter %d values:\n",n);
		for(int i=0;i<n;i++)
		{
			printf("array[%d]=",i);
			scanf("%d",&array[i]);
		}
				
	}
	MPI_Scatter(array,chunk,MPI_INT,&b,chunk,MPI_INT,0,MPI_COMM_WORLD);
	printf("\n%d received in %d\n",b,rank);
	if(b==0 || b==1)
		fact=1;
	else
	{
		while(b!=0)
		{
			fact=fact*b;
			b-=1;
		}		
	}
	MPI_Gather(&fact,1,MPI_INT,factorials,1,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		printf("facts received:\n");
		for(int i=0;i<n;i++)
			{
				printf("%d ",factorials[i]);
			}
			
			for(int i=0;i<n;i++)
			 {
			   sum+=factorials[i];
			 }
			 printf("\nsum of factorials=%d",sum);  
	}
	MPI_Finalize();
	return 0;
} 
