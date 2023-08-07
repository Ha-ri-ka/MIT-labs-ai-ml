#include "mpi.h"
#include <stdio.h>
#include<string.h>
int main(int argc,char *argv[])
{
	int rank,size,i;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	char string[]="HELLO";
	if(string[rank]>=97 && string[rank]<=122)
		{
			string[rank]-=32;
			printf("rank: %d-->%s\n",rank,string);
		}

	else if (string[rank]>=65 && string[rank]<=90)
		{
			string[rank]+=32;
			printf("rank: %d-->%s\n",rank,string);
		}
	MPI_Finalize();
	return 0;
}