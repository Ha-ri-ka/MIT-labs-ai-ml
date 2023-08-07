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
		printf("enter number:");
		scanf("%d",&num);
		for(int i=1;i<size;i++)
		{
			MPI_Ssend(&num,1,MPI_INT,i,0,MPI_COMM_WORLD);
		}
	}
	else
	{
		MPI_Recv(&num,1,MPI_INT,0,0,MPI_COMM_WORLD,&status);
		printf("%d received in process %d\n",num,rank);
	}
	MPI_Finalize();
	return 0;
}
