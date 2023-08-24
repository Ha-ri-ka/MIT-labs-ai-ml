#include<stdio.h>
#include "mpi.h"
#include<string.h>
#include<stdlib.h>
int main(int argc,char * argv[])
{
	int size,rank,i,flag;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int array[size],num;
	if(rank==0)
	{
		printf("enter %d elements:",size);
		for(i=0;i<size;i++)
			scanf("%d",&array[i]);
	}
	MPI_Scatter(array,1,MPI_INT,&num,1,MPI_INT,0,MPI_COMM_WORLD);
	for(i=0;i<num;i++)
	{
		flag=1;
		if(num%i==0)
			flag=0
	}
	
	MPI_Finalize();
	return 0;
} 
