#include "mpi.h"
#include<stdio.h>
int main(int argc,char *argv[])
{
	int rank,size,num;
	MPI_Status status;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	if(rank==0)
	{
		printf("enter the number:");
		scanf("%d",&num);
		MPI_Send(&num,1,MPI_INT,rank+1,rank,MPI_COMM_WORLD);
	}
	else if(rank>=1 && rank<=size-2)
	{
		MPI_Recv(&num,1,MPI_INT,rank-1,rank-1,MPI_COMM_WORLD,&status);
		printf("%d received in process %d\n",num,rank);
		num+=1;
		MPI_Send(&num,1,MPI_INT,rank+1,rank,MPI_COMM_WORLD);
	}
	else if(rank==size-1)
	{
		MPI_Recv(&num,1,MPI_INT,rank-1,rank-1,MPI_COMM_WORLD,&status);
		printf("%d received in process %d\n",num,rank);
	}
	MPI_Finalize();
	return 0;
}