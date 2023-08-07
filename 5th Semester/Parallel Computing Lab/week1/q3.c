#include "mpi.h"
#include <stdio.h>
int main(int argc, char *argv[])
{
	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	int num1=10,num2=5;
	float ans;
	switch(rank)
	{
	case 1:
		ans=num1+num2;
		printf("rank:%d-->%d + %d = %f\n",rank,num1,num2,ans);
		break;
	case 2:
		ans=num1-num2;
		printf("rank:%d-->%d - %d =%f\n",rank,num1,num2,ans);
		break;
	case 3:
		ans=num1/num2;
		printf("rank:%d-->%d / %d =%f\n",rank,num1,num2,ans);
		break;
	case 4:
		ans=num1*num2;
		printf("rank:%d-->%d * %d =%f\n",rank,num1,num2,ans);
		break;
	case 5:
		ans=num1%num2;
		printf("rank:%d-->%d modulus %d =%f\n",rank,num1,num2,ans);
		break;
	default:
		printf("rank:%d-->operator doesnt exist for this rank.\n",rank);
	}
	MPI_Finalize();
	return 0;
}