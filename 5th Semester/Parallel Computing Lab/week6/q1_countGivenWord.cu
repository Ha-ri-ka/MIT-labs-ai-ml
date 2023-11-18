// Write a program in CUDA to count the number of times a given word is repeated in a sentence.
// (Use Atomic function)
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 1024
__global__ void CUDACount(char* A, unsigned int *d_count,char *sub,int len)
{
    int i = threadIdx.x;
    int flag;
    if(A[i]==sub[0])
    {
        flag=1;
        for(int j=1;j<len;j++)
        {
            if(A[i+j]!=sub[j])
            {
                flag=0;
                break;
            }
        }    
    }
    if(flag==1)
    atomicAdd(d_count,1);    
}
int main() 
{
    char A[N],sub[N];
    char *d_A,*d_sub;
    unsigned int *count=0,*d_count,*result;
    count=(unsigned int*)malloc(sizeof(unsigned int));
    result=(unsigned int*)malloc(sizeof(unsigned int));
    printf("enter the string: ");
    scanf("%[^\n]s",A);
    printf("enter substring: ");
    scanf("%[^\n]s",sub);

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventRecord(start, 0);
    
    cudaMalloc((void**)&d_sub, strlen(sub)*sizeof(char));
    cudaMalloc((void**)&d_A, strlen(A)*sizeof(char));
    cudaMalloc((void **)&d_count,sizeof(unsigned int));
    cudaMemcpy(d_sub, sub, strlen(sub)*sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_A, A, strlen(A)*sizeof(char), cudaMemcpyHostToDevice);
    cudaMemcpy(d_count,count,sizeof(unsigned int),cudaMemcpyHostToDevice);
    cudaError_t error =cudaGetLastError();
    if (error != cudaSuccess) 
    {
        printf("CUDA Error1: %s\n", cudaGetErrorString(error));
    }
    CUDACount<<<1,strlen(A)>>>(d_A,d_count,d_sub,strlen(sub));
    error =cudaGetLastError();
    if (error != cudaSuccess) 
    {
        printf("CUDA Error2: %s\n", cudaGetErrorString(error));
    }

    cudaEventRecord(stop, 0);
    cudaEventSynchronize(stop);
    float elapsedTime;
    cudaEventElapsedTime(&elapsedTime, start, stop);

    cudaMemcpy(result, d_count, sizeof(unsigned int), cudaMemcpyDeviceToHost);
    printf("Total occurences of %s=%u\n",sub,*result);
    printf("Time Taken=%f\n",elapsedTime);
    cudaFree(d_A);
    cudaFree(d_sub);
    cudaFree(d_count);
    printf("\n");
    return 0;
}
