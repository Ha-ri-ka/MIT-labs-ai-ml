#include<stdio.h>
#include "mpi.h"
int main(int argc,char * argv[])
{
	int size,rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int m;
	float avg=0,sum=0;
	int array[50],b[50];
	float averages[50];
	if(rank==0)
	{
		printf("enter value of m(chunk):");
		scanf("%d",&m);
		printf("enter %d values:\n",size*m);
		for(int i=0;i<size*m;i++)
		{
			printf("array[%d]=",i);
			scanf("%d",&array[i]);
		} 
	}
	MPI_Bcast(&m,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scatter(array,m,MPI_INT,b,m,MPI_INT,0,MPI_COMM_WORLD);
	for(int i=0;i<m;i++)
	{
		sum+=b[i];
	}
	avg=sum/m;
	fprintf(stdout,"\n%f is average in %d\n",avg,rank);
	fflush(stdout);	
	MPI_Gather(&avg,1,MPI_FLOAT,averages,1,MPI_FLOAT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		int i;
		float tempSum=0,totAvg=0;
		fprintf(stdout,"Averages receievd in root:\n");
		fflush(stdout);
		for(i=0;i<size;i++)
			{
				printf("%f ",averages[i]);
				tempSum+=averages[i];
			}
		totAvg=tempSum/size;
		printf("\ntotal average=%f",totAvg);
	}
	MPI_Finalize();	
	return 0;
} 