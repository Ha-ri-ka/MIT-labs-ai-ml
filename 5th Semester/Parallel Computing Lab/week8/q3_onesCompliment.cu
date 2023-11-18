//%%cuda --name onescomp.cu
#include<stdio.h>
#include<stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

__device__ int onesCompliment(int num)
{
    int onescomp = 0;
    int placeValue = 1;
    int r;
    while (num > 0) {
        int rem = num % 2;
        if(rem==1) r=0;
        else if(rem==0) r=1;
        onescomp = onecomp + r * placeValue;
        placeValue = placeValue * 10;
        num = num / 2;
    }
    return onescomp;
}

__global__ void manipulateValues(int cols,int *mat, int*final)
{
    int m=blockDim.x;
    int row=blockIdx.x*blockDim.x+threadIdx.x;
    int i,k;
    if(row<m)
    {
        if(row!=0 && row!=m-1) //border rows 
        {
            for(i=0;i<cols;i++)
            {
                k=row*m+i;
                if(i!=0 && i!=cols-1) //border columns                
                    final[k]=onesCompliment(mat[k]);                
                else
                    final[k]=mat[k];
            }            
        }
        else
        {
            for(i=0;i<cols;i++)
            {              
                k=row*m+i;
                final[k]=mat[k];                
            }     
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
    manipulateValues<<<1,m>>>(n,d_mat,d_final);

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
