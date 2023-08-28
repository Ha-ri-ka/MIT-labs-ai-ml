// Write a program in CUDA to add two vectors of length N using
// a) block size as N
// b) N threads
#include<stdio.h>	
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
__global__ void add(int *a, int *b, int *c)
{    
    int tid=(blockIdx.x*blockDim.x)+threadIdx.x;
    printf("blockid:%d,threadid:%d\n",blockIdx.x,threadIdx.x);
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
    printf("\nEnter matrix B:\n");
    for(i=0;i<n;i++)
    {
        printf("b[%d]=",i);
        scanf("%d",&b[i]);
    }
    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
    //1 block
    dim3 dimGrid(1,1,1);
    //n blocks
    //dim3 dimGrid(n,1,1);
    //n threads per block
    dim3 dimBlock(n,1,1);
    //1 thread per block
    //dim3 dimBlock(1,1,1);
    add<<<dimGrid,dimBlock>>>(d_a, d_b, d_c);	
    cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for(i=0;i<n;i++)
    printf("%d ",c[i]);
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}