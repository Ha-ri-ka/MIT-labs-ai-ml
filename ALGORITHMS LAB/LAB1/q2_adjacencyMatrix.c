#include<stdio.h>
void main()
{
    int vertices,i,j;
    printf("enter number of vertices:"); 
    scanf("%d",&vertices);
    int adjacencyMatrix[vertices+1][vertices+1];
    adjacencyMatrix[0][0]=-1;
    printf("enter vertices:\n");
    for(j=1;j<vertices+1;j++)
    {
        scanf("%d",&adjacencyMatrix[0][j]);
    }
    for(i=1;i<vertices+1;i++)
    {
        adjacencyMatrix[i][0]=adjacencyMatrix[0][i];
    }
    printf("enter 1 if an edge exists, 0 if it doesnt\n");
    for(i=1;i<vertices+1;i++)
    {
        for(j=1;j<vertices+1;j++)
        {
            jump:
            printf("between %d and %d:",adjacencyMatrix[0][i],adjacencyMatrix[j][0]);
            scanf("%d",&adjacencyMatrix[i][j]);
            if(adjacencyMatrix[i][j]!=1 && adjacencyMatrix[i][j]!=0)
            {
                printf("invalid input enter again\n");
                goto jump;
            }
        }        
    }
    printf("adjacency matrix is:\n");
    for(i=0;i<vertices+1;i++)
    {
        for(j=0;j<vertices+1;j++)
        printf("%d  ",adjacencyMatrix[i][j]);
        printf("\n");        
    }
}
