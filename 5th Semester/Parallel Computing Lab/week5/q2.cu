// Implement a CUDA program to add two vectors of length N by keeping the number of
// threads per block as 256 (constant) and vary the number of blocks to handle N elements.
#include<stdio.h>	
#include<math.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
__global__ void add(int *a, int *b, int *c)
{    
    int tid=(blockIdx.x*blockDim.x)+threadIdx.x;
    //printf("blockid:%d,threadid:%d\n",blockIdx.x,threadIdx.x);
    c[tid]=a[tid]+b[tid];
}		
int main(void) 
{
    int n;
    printf("Enter size of array:"); 
    scanf("%d",&n);
    int size = n * sizeof(int);
    int a[n], b[n], c[n], i;
    int *d_a, *d_b, *d_c;
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);
    printf("\nEnter matrix A:\n");
    for(i=0;i<n;i++)
    {
        printf("a[%d]=",i);
        scanf("%d",&a[i]);
    }
    printf("Enter matrix B:\n");
    for(i=0;i<n;i++)
    {
        printf("b[%d]=",i);
        scanf("%d",&b[i]);
    }
    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
    //efficient dimensions
    dim3 eff_dimGrid(ceil(n/256.0),1,1);
    dim3 eff_dimBlock(256,1,1);
    //1 block n threads
    dim3 a_dimGrid(1,1,1);
    dim3 a_dimBlock(n,1,1);
    //n blocks 1 thread in each
    dim3 b_dimGrid(n,1,1);
    dim3 b_dimBlock(1,1,1);
    printf("\nEfficient thread and block creation.\n");
    add<<<eff_dimGrid,eff_dimBlock>>>(d_a, d_b, d_c);
    printf("Result:\n");
    for(i=0;i<n;i++)
    printf("%d ",c[i]);
    printf("\n1 block with n threads.\n");
    add<<<a_dimGrid,a_dimBlock>>>(d_a, d_b, d_c);
    printf("Result:\n");
    for(i=0;i<n;i++)
    printf("%d ",c[i]);
    printf("\nN block with 1 thread in each.\n");
    add<<<b_dimGrid,b_dimBlock>>>(d_a, d_b, d_c);	
    cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for(i=0;i<n;i++)
    printf("%d ",c[i]);    
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}