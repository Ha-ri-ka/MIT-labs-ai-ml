#include "mpi.h"
#include<stdio.h>
int main(int argc,char *argv[])
{
	int rank,size,num;
	MPI_Status status;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int array[size];
	int buffer_size=100;
	int buffer[buffer_size];
	MPI_Buffer_attach(buffer,buffer_size);
	if(rank==0)
	{
		printf("enter the array elements:\n");
		for(int i=0;i<size;i++)
		{
			printf("array[%d]= ",i);
			scanf("%d",&array[i]);
		}
		for(int i=1;i<size;i++)
		{
			MPI_Bsend(&array[i],1,MPI_INT,i,i,MPI_COMM_WORLD);
		}
	}
	else
	{
		MPI_Recv(&num,1,MPI_INT,0,rank,MPI_COMM_WORLD,&status);
	}
	if(rank%2==0)
		{
			printf("rank %d-->%d ^ 2=%d\n",rank,num,num*num);
		}
		else
		{
			printf("rank %d-->%d ^ 3=%d\n",rank,num,num*num*num);	
		}
	MPI_Buffer_detach(buffer,&buffer_size);
	MPI_Finalize();
}