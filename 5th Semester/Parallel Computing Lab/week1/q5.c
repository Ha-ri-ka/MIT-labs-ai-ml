#include "mpi.h"
#include<stdio.h>
int factorial(int x)
{
	int ans=1;
	if (x==0)
		return 1;	
	while(x!=0)
	{
		ans*=x;
		x-=1;
	}
	return ans;
}

void fibonacci(int x)
{
	int i, n;
	int t1 = 0, t2 = 1;
    int nextTerm = t1 + t2;
    if (x==1)
    	printf("Fibonacci Series: 0");
    else	
  		printf("Fibonacci Series: %d, %d, ", t1, t2);
  	for (i = 3; i <= x; ++i) {
    printf("%d, ", nextTerm);
    t1 = t2;
    t2 = nextTerm;
    nextTerm = t1 + t2;
  }
}

int main(int argc, char *argv[])
{
	int rank,size;
	MPI_Init(&argc,&argv);
	int ans;
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	if(rank%2==0)
		{
			ans=factorial(rank);
			printf("\nrank:%d-->%d!=%d",rank,rank,ans);
		}
	else if (rank%2!=0)
		{
			printf("\nrank:%d-->",rank);
			fibonacci(rank);
		}
	MPI_Finalize();
	return 0;
}