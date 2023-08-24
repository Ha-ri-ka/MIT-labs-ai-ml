#include<stdio.h>
#include "mpi.h"
int main(int argc,char * argv[])
{
	int size,rank,i,j;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int matrix[4][4],b[4],sumRow[4],final[4][4];
	if(rank==0)
	{
		printf("enter 4x4 matrix:");
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				printf("matrix[%d][%d]=",i,j);
				scanf("%d",&matrix[i][j]);
			}
		}

		printf("\ninput matrix:\n");
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				printf("%d ",matrix[i][j]);
			}
			printf("\n");
		}
	}
	MPI_Scatter(matrix,4,MPI_INT,b,4,MPI_INT,0,MPI_COMM_WORLD);
	//printf("\nrow in rank %d:",rank);
	for(i=0;i<4;i++)
	//	{
	//		printf("%d  ",b[i]);
			MPI_Scan(&b[i],&sumRow[i],1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
	//	}
	//printf("\nsumRow in rank %d:",rank);
	//for(i=0;i<4;i++)
	//	printf("%d  ",sumRow[i]);
	MPI_Gather(sumRow,4,MPI_INT,final,4,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		printf("\nfinal matrix:\n");
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				printf("%d ",final[i][j]);
			}
			printf("\n");
		}
	}


	MPI_Finalize();
	return 0;
} 
