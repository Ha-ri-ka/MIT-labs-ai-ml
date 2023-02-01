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
        else if(ele>root->value) 
            root->right=create_bst(root->right,ele); 
        else 
            printf("duplicates not allowed\n");
    }
    return root;
 }
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
struct node* insert(struct node *root,int key)
{
    struct node*prev=NULL;
    struct node*temp=root;
    while(temp)
    {
        prev=temp;
        if(key< temp->value)
        temp=temp->left;
        else
        temp=temp->right;
    }
    struct node*new=getnode(key);
    if(key<prev->value)
    prev->left=new;
    else
    prev->right=new;
    return(root);
}
//-----------------------
void main()
{
    struct node *root=NULL;
    int ch,ele,key;
    printf("enter 1 to start or continue creating tree,enter -1 to stop at any time.");
    printf("enter choice:"); scanf("%d",&ch);
    if(ch!=-1)
    {
    do
    {
            printf("enter data: ");
            scanf("%d", &ele);
            root = create_bst(root, ele);
            printf("enter choice: ");
            scanf("%d", &ch);
    } while (ch != -1);
    }
    else
    exit(0);
    
    printf("preorder traversal:\n"); preorder(root);
    printf("\ninorder traversal:\n"); inorder(root);
    printf("\npost order traversal:\n"); postorder(root);
    
    printf("\nenter element to search for:");
    scanf("%d",&key);
    struct node *keynode=search(root,key);
    if(keynode==NULL)
    {
        root=insert(root,key);
        printf("The element %d is added to the tree.",key);
        printf("The new tree is:\n");
        inorder(root);
    }
    else
    printf("%d exists in the tree",keynode->value);
}
