//%%cuda --name spvm.cu
#include<stdio.h>
#include<stdlib.h>
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

__global__ void parallelSpVM(int n,int *data,int *col_ind,int *row_ptr,int *x,int *final)
{
    int ele_ind;
    int prod,row_start,row_end;
    int row=blockIdx.x*blockDim.x+threadIdx.x;
    if(row<n)
    {
        //printf("\n%d\n",row);
        prod=0;
        row_start=row_ptr[row];
        row_end=row_ptr[row+1];
        //printf("\nrow_start=%d,row_end=%d",row_start,row_end);
        for(ele_ind=row_start;ele_ind<row_end;ele_ind++)
        {
            //printf("\ndata=%d,x=%d,ele_ind=%d\n",data[ele_ind],x[ele_ind],ele_ind);
            prod+=data[ele_ind]*x[col_ind[ele_ind]];
        }
        //printf("\n%d\n",prod);
        final[row]=prod;
    }
}

int main()
{
    int n;
    printf("Enter the dimension of the sparse matrix (square):");
    scanf("%d",&n);
    //host variables
    int *sparse=(int*)malloc(sizeof(int)*n*n);
    int *data=(int*)malloc(sizeof(int)*n*n);
    int *col_ptr=(int*)malloc(sizeof(int)*n*n);
    int *row_ptr=(int*)malloc(sizeof(int)*(n+1));
    int *x=(int*)malloc(sizeof(int)*n);
    int *final=(int*)malloc(sizeof(int)*n);

    int i,j,k,l=0;
    int nonZeroCount=0;
    printf("enter sparse matrix:\n");
    for(i=0;i<n;i++)
    {
        row_ptr[l]=nonZeroCount;
        l++;
        for(j=0;j<n;j++)
        {
            k=i*n+j;
            scanf("%d",&sparse[k]);
            if(sparse[k]!=0)
            {
                data[nonZeroCount]=sparse[k];
                col_ptr[nonZeroCount]=j;
                nonZeroCount+=1;
            }
        }
    }
    row_ptr[n]=nonZeroCount;

    printf("\ndata array:\n");
    for (i = 0; i < nonZeroCount; i++)
        printf("%d ",data[i]);
    printf("\ncol_ind array:\n");
    for (i = 0; i < nonZeroCount; i++)
        printf("%d ",col_ptr[i]);
    printf("\nrow_ptr array:\n");
    for (i = 0; i < n+1; i++)
        printf("%d ",row_ptr[i]);

    printf("\nenter column vector:");
    for ( i = 0; i < n; i++)
        scanf("%d",&x[i]);
        
    //device variables
    int *d_data,*d_col_ptr,*d_row_ptr,*d_x,*d_final;
    cudaMalloc((void**)&d_data,sizeof(int)*nonZeroCount);
    cudaMalloc((void**)&d_col_ptr,sizeof(int)*nonZeroCount);
    cudaMalloc((void**)&d_row_ptr,sizeof(int)*(n+1));
    cudaMalloc((void**)&d_x,sizeof(int)*n);
    cudaMalloc((void**)&d_final,sizeof(int)*n); 
  
    //copying values to device variables
    cudaMemcpy(d_data,data,sizeof(int)*nonZeroCount,cudaMemcpyHostToDevice); 
    cudaMemcpy(d_col_ptr,col_ptr,sizeof(int)*nonZeroCount,cudaMemcpyHostToDevice); 
    cudaMemcpy(d_row_ptr,row_ptr,sizeof(int)*(n+1),cudaMemcpyHostToDevice); 
    cudaMemcpy(d_x,x,sizeof(int)*n,cudaMemcpyHostToDevice); 

    //kernel Launch
    parallelSpVM<<<1,n>>>(n,d_data,d_col_ptr,d_row_ptr,d_x,d_final);

    cudaMemcpy(final,d_final,sizeof(int)*n,cudaMemcpyDeviceToHost);

    printf("\nResult:\n");
    for(int i = 0; i < n;i++)
      printf("%d ",final[i]);   
  
    cudaFree(d_x);
    cudaFree(d_final);
    cudaFree(d_data);
    cudaFree(d_row_ptr);
    cudaFree(d_col_ptr);    
    return 0;
}
