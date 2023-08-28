// Write a program in CUDA which performs convolution operation on one dimensional input
// array N of size width using a mask array M of size mask_width to produce the resultant one
// dimensional array P of size width.
#include<stdio.h>	
#include<math.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
__global__ void convulution(int *n, int *m, int *p, int len, int maskLength)
{    
    int tid=(blockIdx.x*blockDim.x)+threadIdx.x;
    int j;
    //printf("blockid:%d,threadid:%d\n",blockIdx.x,threadIdx.x);
    float pvalue=0;
    int start=tid-(maskLength/2);
    for(j=0;j<maskLength;j++)
    {
        if(start+j>=0 && start+j<=len)
        {
            pvalue+=n[start+j]*m[j];
        }
    }
    p[tid]=pvalue;
}		
int main(void) 
{
    int len,mask_width;
    printf("Enter size of array:"); 
    scanf("%d",&len);
    printf("Enter mask width:");
    scanf("%d",&mask_width);
    int size = len * sizeof(int);
    int a[len],m[mask_width], p[len], i;
    int *d_a, *d_m, *d_p;
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_m, size);
    cudaMalloc((void **)&d_p, size);
    printf("\nEnter array:\n");
    for(i=0;i<len;i++)
    {
        //printf("a[%d]=",i);
        scanf("%d",&a[i]);
    }
    printf("Enter mask\n");
    for(i=0;i<mask_width;i++)
    {
        //printf("mask[%d]=",i);
        scanf("%d",&m[i]);
    }
    cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_m, &m, size, cudaMemcpyHostToDevice);
    dim3 dimGrid(ceil(len/256.0),1,1);
    dim3 dimBlock(256,1,1);
    convulution<<<dimGrid,dimBlock>>>(d_a, d_m, d_p,len,mask_width);	
    cudaMemcpy(p, d_p, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for(i=0;i<len;i++)
    printf("%d ",p[i]);
    cudaFree(d_a);
    cudaFree(d_m);
    cudaFree(d_p);
    return 0;
}