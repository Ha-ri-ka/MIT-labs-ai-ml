#include<stdio.h>
#include<stdlib.h>
//-----------------------
struct node
{
int value;
struct node *right;
struct node *left;
};
//-----------------------
struct node * getnode(int ele)
{
    struct node * temp=malloc(sizeof(struct node));
    temp->value=ele;
    temp->left=NULL;
    temp->right=NULL;
    return (temp);
}
//-----------------------
void inorder(struct node* temp) 
{
    if(temp)
    {
        inorder(temp->left);
        printf("%d ",temp->value);
        inorder(temp->right);
    }
}
//-----------------------
struct node *tree()
{
                /*5
                  /\
                3   6
               /\
              1  4 */
    struct node* n5=getnode(5);
    struct node* n3=getnode(3); 
    struct node* n6=getnode(6);
    struct node* n1=getnode(1);
    struct node* n4=getnode(4);
    n5->left=n3;
    n5->right=n6;
    n3->left=n1;
    n3->right=n4;
    return(n5);
}
//-----------------------
struct node*create_bt()
{
    struct node*newnode; int d;
    newnode=(struct node*)malloc(sizeof(struct node));
    scanf("%d",&d);
    if(d==-1)
    return NULL;
    newnode->value=d;
    printf("enter left of %d:",newnode->value);
    newnode->left=create_bt();
    printf("enter right of %d:",newnode->value);
    newnode->right=create_bt();
    return newnode;
}
//-----------------------
struct node*create_bst(struct node*root,int ele)
 {
    if(root==NULL)
    {
        root=getnode(ele);
        return root;
    }
    else
    {
        if (ele < root->value) 
            root->left = create_bst(root->left, ele); 
        else if(ele>root->value) 
            root->right=create_bst(root->right,ele); 
        else 
            printf("duplicates not allowed\n");
    }
    return root;
 }
