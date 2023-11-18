//%%cuda --name rowman.cu
#include<stdio.h>
#include<stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

__global__ void manipulateRows(int cols,int *mat, int*final)
{
    int m=blockDim.x;
    int row=blockIdx.x*blockDim.x+threadIdx.x;
    int i,k;
    if(row<m)
    {
        for(i=0;i<cols;i++)
        {
            k=row*m+i;
            final[k]=pow(mat[k],row+1);
        }
    }
}

int main()
{
    int m,n;
    printf("Enter number of rows:");
    scanf("%d",&m);
    printf("Enter number of columns:");
    scanf("%d",&n);
    //host variables
    int *mat=(int*)malloc(sizeof(int)*m*n);
    int *final=(int*)malloc(sizeof(int)*n);

    int i,j,k;
    printf("enter matrix row-wise:\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            k=i*n+j;
            scanf("%d",&mat[k]);
        }
    }
            
    //device variables
    int *d_mat,*d_final;
    cudaMalloc((void**)&d_mat,sizeof(int)*m*n); 
    cudaMalloc((void**)&d_final,sizeof(int)*m*n); 
    
    //copying values to device variables
    cudaMemcpy(d_mat,mat,sizeof(int)*m*n,cudaMemcpyHostToDevice); 


    //kernel Launch
    manipulateRows<<<1,m>>>(n,d_mat,d_final);

    cudaMemcpy(final,d_final,sizeof(int)*m*n,cudaMemcpyDeviceToHost);

    printf("\nResult:\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            k=i*m+j;
            printf("%d ",final[k]);
        }
        printf("\n");
    }
      
    cudaFree(d_mat);
    cudaFree(d_final);   
    return 0;
}
