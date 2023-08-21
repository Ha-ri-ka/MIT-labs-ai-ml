#include<stdio.h>
#include "mpi.h"
int main(int argc,char * argv[])
{
	int size,rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Errhandler_set(MPI_COMM_WORLD,MPI_ERRORS_RETURN);
	int num,fact=1,sum=0;
	int errcode1,errcode2,len;
	char errstring[50];
	num=rank+1;
	errcode1=MPI_Scan(&num,&fact,1,MPI_INT,MPI_PROD,MPI_COMM_WORLD);
	if(errcode1!=MPI_SUCCESS)
	{
		printf("error in facorial computation.");
		MPI_Error_string(errcode1,errstring,&len);
		printf("%s",errstring);
	}
	printf("rank %d: %d!=%d\n",rank,num,fact);
	errcode2=MPI_Scan(&fact,&sum,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
	if(errcode2!=MPI_SUCCESS)
	{
		printf("error in facorial sum computation.");
		MPI_Error_string(errcode2,errstring,&len);
		printf("%s",errstring);
	}
	printf("rank %d partial sum: %d\n",rank,sum);
	if(rank==size-1)
	{
		printf("Final sum of 1!+2!+..+%d!=%d",size,sum);
	}
	MPI_Finalize();
	return 0;
} 
