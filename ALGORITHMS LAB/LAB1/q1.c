#include<stdio.h>
#include"tree.c"
//-----------------------
struct node * search(struct node * root,int key)
{
    if(root==NULL)
    return NULL;
    if(root->value==key)
    return root;
    else if(root->value>key)
    return (search(root->left,key)); 
    else
    return(search(root->right,key)); 
}
//-----------------------
struct node* create_bst(struct node*root,int ele)
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
        else if (ele > root->value)
            root->right = create_bst(root->right, ele);
        else
            printf("no");
    }
    return root;
}
void main()
{
    struct node *root=NULL;
    int ch,ele;
    do
    {
        printf("enter data: "); scanf("%d",&ele);
        root=create_bst(root,ele);
        scanf("%d",&ch);
    }while(ch!=-1);
    int key;
    inorder(root);
    printf("\nenter element to search for:");
    scanf("%d",&key);
    struct node *keynode=iterative_search(root,key);
    if(keynode==NULL)
    printf("the element does not exist in tree");
    else
    printf("%d exists in the tree",keynode->value);
}
