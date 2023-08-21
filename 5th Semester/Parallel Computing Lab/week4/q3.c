#include<stdio.h>
#include "mpi.h"
int main(int argc,char * argv[])
{
	int size,rank,i,j;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int matrix[3][3],key,row[3],count=0,rowWiseCount[3];
	if(rank==0)
	{
		printf("enter 3x3 matrix:\n");
		for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				printf("matrix[%d][%d]=",i,j);
				scanf("%d",&matrix[i][j]);
			}
		}
		printf("\nenter key value:");
		scanf("%d",&key); 
	}
	MPI_Scatter(matrix,3,MPI_INT,row,3,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Bcast(&key,1,MPI_INT,0,MPI_COMM_WORLD);
	printf("\nrow in rank %d:",rank);
	for(i=0;i<3;i++)
		{
			printf("%d ",row[i]);
			if(row[i]==key)
			count++;
		}
	MPI_Gather(&count,1,MPI_INT,rowWiseCount,1,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		int totSum=0;
		printf("\nrow wise counts gathered:");
		for(i=0;i<3;i++)
		{
			printf("%d ",rowWiseCount[i]);
			totSum+=rowWiseCount[i];
		} 
		printf("\nTotal number of occurences of %d: %d",key,totSum);
	}

	MPI_Finalize();
	return 0;
} 
