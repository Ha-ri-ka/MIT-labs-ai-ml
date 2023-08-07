#include "mpi.h"
#include<stdio.h>
int main(int argc, char *argv[])
{
	int rank,size;
	//initializing the envronment
	MPI_Init(&argc,&argv);
	int x=10;
	float ans;
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(rank%2==0)
		printf("%d rank-->hello\n",rank);
	else if (rank%2!=0)
		printf("%d rank-->world\n",rank);
	MPI_Finalize();
	return 0;
}