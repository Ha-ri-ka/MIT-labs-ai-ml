// Write a program to construct a binary tree to support the following operations. 
//   Assume no duplicate elements while constructing the tree. 
//  i. Given a key, perform a search in the binary search tree. If the key is found 
// then display “key found” else insert the key in the binary search tree. 
//  ii. Display the tree using inorder, preorder and post order traversal methods 
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
void preorder(struct node* root)
{
    if(root)
    {
        printf("%d ",root->value);
        preorder(root->left);
        preorder(root->right);
    }
}
//-----------------------
void postorder(struct node* root)
{
    if(root)
    {        
        postorder(root->left);
        postorder(root->right);
        printf("%d ",root->value);
    }
}
//-----------------------
struct node* create_tree()
{
    struct node*newnode; int d;
    newnode=(struct node*)malloc(sizeof(struct node));
    scanf("%d",&d);
    if(d==-1)
    return NULL;
    newnode->value=d;
    printf("enter left of %d:",newnode->value);
    newnode->left=create_tree();
    printf("enter right of %d:",newnode->value);
    newnode->right=create_tree();
    return newnode;
}
 //-----------------------
 int search(struct node *root,int key)
{
    if(root==NULL)
    return 0;
    if(root->value==key)
    return 1;
    if(search(root->left,key)||search(root->right,key))
    return 1;
}
//-----------------------
struct node *insert(struct node*root,int key,int p)
{
    struct node *new=(struct node*)malloc(sizeof(struct node));
    new->value=key;
    new->left=new->right=NULL;
    struct node *temp=root;
    if(p==1)
    {
        while(temp->left!=NULL)
        temp=temp->left;
        temp->left=new;
    }
    else
    {
        while(temp->right!=NULL)
        temp=temp->right;
        temp->right=new;
    }
    return root;
}
//-----------------------
void main()
{
    struct node *root=NULL;
    int ch,ele,key,res,p;
    printf("enter head node to start creating tree,enter -1 to stop at any time.");
    root=create_tree(); 
    printf("enter element to search for:");
    scanf("%d",&key);
    res=search(root,key);
    if(res==0)
    {
        printf("element doesnt exist in tree.Which subtree would u like to insert in?(L->1 or R->0):");
        scanf("%d",&p);
        root=insert(root,key,p);
        printf("The element %d is added to the tree.",key);
        printf("The new tree is:\n");
        inorder(root);
    }
    else
    printf("%d exists in the tree",key);
    printf("\npreorder traversal:\n"); preorder(root);
    printf("\ninorder traversal:\n"); inorder(root);
    printf("\npost order traversal:\n"); postorder(root);
}
