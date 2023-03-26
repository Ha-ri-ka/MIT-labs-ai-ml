#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
} *head;

int main()
{
    int vertices, edges,i,j;
    struct node *temp;
    printf("\nEnter number of vertices: ");
    scanf("%d", &vertices);
    struct node *A[vertices];
    
    for (i = 0; i < vertices; i++)
    {
        printf("\nEnter the number of edges for vertex:");
        scanf("%d", &edges);
        head = (struct node *)malloc(sizeof(struct node));
        printf("\nEnter the vertex:");
        scanf("%d", &head->data);
        head->next = NULL;
        temp = head;
        for (j = 0; j < edges; j++)
        {
            struct node *new = (struct node *)malloc(sizeof(struct node));
            printf("\nEnter the linked vertex:");
            scanf("%d", &new->data);
            new->next = NULL;
            temp->next = new;
            temp = new;
        }
        A[i] = head;
    }

    for ( i = 0; i < vertices; i++)
    {
        struct node *p;
        p = A[i];
        while (p != NULL)
        {
            printf("%d\t", p->data);
            p = p->next;
        }
        printf("\n");
    }
    return 0;
}
