#include "mpi.h"
#include<stdio.h>
#include<math.h>
int main(int argc, char *argv[])
{
	int rank,size;
	//initializing the envronment
	MPI_Init(&argc,&argv);
	int x=10;
	float ans;
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	ans=pow(x,rank);
	printf("%d to the power %d=%f\n",x,rank,ans);
	MPI_Finalize();
	return 0;
}