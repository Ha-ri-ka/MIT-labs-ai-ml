#include<stdio.h>
#include "mpi.h"
#include <string.h>
#include <stdlib.h>
int main(int argc,char * argv[])
{
	int size,rank;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	char string[50],b[50];
	int consCount[size];
	int chunk,ccount=0;
	if(rank==0)
	{
		printf("Enter your string:");
		scanf("%s",string);
		if(strlen(string)%size!=0)
		{
			fprintf(stdout,"Cannot perform vowel count due to incompatibility of number of processes and string length");
			fflush(stdout);
			exit(0);
		}
		chunk=strlen(string)/size;
		//printf("string entered:%s",string);
	}
	MPI_Bcast(&chunk,1,MPI_INT,0,MPI_COMM_WORLD);
	MPI_Scatter(string,chunk,MPI_CHAR,b,chunk,MPI_CHAR,0,MPI_COMM_WORLD);
	for(int i=0;i<chunk;i++)
	{
		if(b[i]!='a'&&b[i]!='e'&&b[i]!='i'&&b[i]!='o'&&b[i]!='u')
			ccount+=1;
	} 
	MPI_Gather(&ccount,1,MPI_INT,consCount,1,MPI_INT,0,MPI_COMM_WORLD);
	if(rank==0)
	{
		int totcons=0;
		fprintf(stdout,"consonants counts received in root:\n");
		fflush(stdout);
		for(int i=0;i<size;i++)
			{
				printf("%d ",consCount[i]);
				totcons+=consCount[i];
			}
		printf("\nTotal number of consonants in the string:%d",totcons);
	}
	MPI_Finalize();
	return 0;
} 