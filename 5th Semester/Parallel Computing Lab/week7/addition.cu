//%%cuda --name addition.cu
#include <stdio.h>
#include<stdlib.h>
#include<cuda_runtime.h>
__global__ void addRow(int *mat1,int *mat2, int *final, int cols)
{
    int tid=blockIdx.x*blockDim.x+threadIdx.x;
    int row;
    if(tid!=0)
      row=tid+cols;
    else if(tid==0)
      row=0;
    int i,k;
    for(i=0;i<cols;i++)
    {
        k=row+i;
        final[k]=mat1[k]+mat2[k];
    }
}
__global__ void addCol(int *mat1,int *mat2, int *final, int rows)
{
    int tid=blockIdx.x*blockDim.x+threadIdx.x;
    int cols=blockDim.x;
    int i,k;
    final[tid]=mat1[tid]+mat2[tid];
    for(i=0;i<rows-1;i++)
    {
        k=tid+cols;
        final[k]=mat1[k]+mat2[k];
    }
}
__global__ void addEles(int *mat1,int *mat2,int *final)
{
    int tid=blockIdx.x*blockDim.x+threadIdx.x;
    final[tid]=mat1[tid]+mat2[tid];
}
int main()
{
    int r,c,i,j,k;
    printf("number of rows: "); 
    scanf("%d",&r);
    printf("enter number of columns: ");
    scanf("%d",&c);
    int * mat1=(int*)malloc(sizeof(int)*r*c);
    int * mat2=(int*)malloc(sizeof(int)*r*c);
    int * final=(int*)malloc(sizeof(int)*r*c);
    printf("enter matrix 1:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            k = i * r + j;
            scanf("%d", &mat1[k]);
        }
    }
    printf("enter matrix 2:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            k = i * r + j;
            scanf("%d", &mat2[k]);
        }
    }

    int * d_mat1,*d_mat2,*d_final;
    cudaMalloc((void**)&d_mat1,sizeof(int)*r*c);
    cudaMalloc((void**)&d_mat2,sizeof(int)*r*c);
    cudaMalloc((void**)&d_final,sizeof(int)*r*c);

    cudaMemcpy(d_mat1,mat1,sizeof(int)*r*c,cudaMemcpyHostToDevice);
    cudaMemcpy(d_mat2,mat2,sizeof(int)*r*c,cudaMemcpyHostToDevice);

    printf("Each thread calculates one row\n")
    addRow<<<1,r>>>(d_mat1,d_mat2,d_final,c);
    cudaMemcpy(final,d_final,sizeof(int)*r*c,cudaMemcpyDeviceToHost);
    printf("resultant matrix:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        printf("%d ",final[i]);
        printf("\n");
    }

    printf("Each thread calculates one column\n");
    addCol<<<1,c>>>(d_mat1,d_mat2,d_final,r);
    cudaMemcpy(final,d_final,sizeof(int)*r*c,cudaMemcpyDeviceToHost);
    printf("resultant matrix:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        printf("%d ",final[i]);
        printf("\n");
    }

    printf("Each thread calculates one Element\n");
    addEles<<<1,r*c>>>(d_mat1,d_mat2,d_final);
    cudaMemcpy(final,d_final,sizeof(int)*r*c,cudaMemcpyDeviceToHost);
    printf("resultant matrix:\n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        printf("%d ",final[i]);
        printf("\n");
    }

    cudaFree(d_mat1);
    cudaFree(d_mat2);
    cudaFree(d_final);
    return 0;
}
