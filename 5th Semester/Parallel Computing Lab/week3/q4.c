#include<stdio.h>
#include "mpi.h"
#include<string.h>
#include<stdlib.h>
int main(int argc,char * argv[])
{
	int size,rank,i;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	char string1[50],string2[50],sub1[50],sub2[50],concat[50];
	char final[100];
	int chunk;	
	if(rank==0)
	{
		jump:
		printf("enter string 1:");
		scanf("%s",string1);
		printf("enter string2:");
		scanf("%s",string2);
		if(strlen(string2)!=strlen(string1))
		{
			printf("Enter strings of same length.");
			goto jump;
		}
		if(strlen(string2)%size!=0)
		{
			printf("Cannot perform operation with %d number of processes.\nTerminating.",size);
			exit(0);
		}
		chunk=strlen(string1)/size;
	}
	MPI_Bcast(&chunk,1,MPI_INT,0,MPI_COMM_WORLD);
   	MPI_Scatter(string1,chunk,MPI_CHAR,sub1,chunk,MPI_CHAR,0,MPI_COMM_WORLD);
	MPI_Scatter(string2,chunk,MPI_CHAR,sub2,chunk,MPI_CHAR,0,MPI_COMM_WORLD);
	//printf("\nstring in rank %d=%s,%s",rank,sub1,sub2);
	for(i=0;i<=2*chunk;i+=2)
	{
		concat[i]=sub1[i/2];
		concat[i+1]=sub2[i/2];
	}
	concat[2*chunk]='\0';
	MPI_Gather(concat,2*chunk,MPI_CHAR,final,2*chunk,MPI_CHAR,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		printf("\nFinal string:%s",final);
	}	
	MPI_Finalize();
	return 0;
} 
