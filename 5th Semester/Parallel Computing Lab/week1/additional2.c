#include<stdio.h>
#include "mpi.h"
#include<string.h>
#include<stdlib.h>
int main(int argc,char * argv[])
{
	int size,rank,i,j,flag,k;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int primes[50];
	if(size<2)
	{
		printf("Program requires 2 processes.\nTerminating.");
		exit(0);
	}
	if(rank==0)
	{
		k=0;
		for(i=1;i<50;i++)
		{
			flag=1;
			for(j=2;j<i;j++)
			{
				if(i%j==0)
					flag=0;
			}
			if(flag)
				{
					primes[k]=i;
					k++;
				}
		}
		printf("prime numbers from 1 to 49 computed in rank 0:");
		for(i=0;i<k;i++)
			printf("%d ",primes[i]);
	}
	if(rank==1)
	{
		k=0;
		for(i=50;i<100;i++)
		{
			flag=1;
			for(j=2;j<i;j++)
			{
				if(i%j==0)
					flag=0;
			}
			if(flag)
				{
					primes[k]=i;
					k++;
				}
		}
		printf("\nprime numbers from 50 to 100 computed in rank 1:");
		for(i=0;i<k;i++)
			printf("%d ",primes[i]);
	}
	MPI_Finalize();
	return 0;
} 
