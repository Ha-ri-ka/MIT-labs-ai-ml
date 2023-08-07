#include "mpi.h"
#include<stdio.h>
#include<string.h>

int main(int argc,char *argv[])
{
	int rank,size,len,i;
	MPI_Status status;
	char word[50];
	
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(rank==0)
	{
		printf("enter the word:");
		scanf("%s",word);
		len=strlen(word);
		MPI_Ssend(&len,1,MPI_INT,1,0,MPI_COMM_WORLD);
		MPI_Ssend(&word,len,MPI_CHAR,1,1,MPI_COMM_WORLD);
		MPI_Recv(&word,len,MPI_CHAR,1,2,MPI_COMM_WORLD,&status);
		printf("\n%s received from process1 in process0",word);
	}
	else if(rank==1)
	{
		MPI_Recv(&len,1,MPI_INT,0,0,MPI_COMM_WORLD,&status);
		MPI_Recv(&word,len,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);
		printf("\n%s received from process0 in process1",word);		
		for(int i=0;i<strlen(word);i++)
		{
		if(word[i]>=97 && word[i]<=122)
		{
			word[i]-=32;
		}

			else if (word[i]>=65 && word[i]<=90)
		{
			word[i]+=32;
		}
	}
		MPI_Ssend(&word,len,MPI_CHAR,0,2,MPI_COMM_WORLD);
	}
	MPI_Finalize();
	return 0;
}
