//  Write a program to construct a binary tree to support the following operations.
//  Assume no duplicate elements while constructing the tree.
//  i. Given a key, perform a search in the binary search tree. If the key is found
// then print “key found” else insert the key in the binary search tree.
//  ii. display the tree using inorder, preorder and post order traversal methods
#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node *right;
    struct node *left;
} node;

node *get_node(int data)
{
    node *newNode = (node *)malloc(sizeof(node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

node *create_bst(node *root, int ele)
{
    if (root == NULL)
    {
        root = get_node(ele);
        return root;
    }
    else
    {
        if (ele < root->data)
            root->left = create_bst(root->left, ele);
        else if (ele > root->data)
            root->right = create_bst(root->right, ele);
        else
            printf("no duplicates allowed\n");
    }
    return root;
}

void inorder(node *root)
{
    if (root)
    {
        inorder(root->left);
        printf("%d  ", root->data);
        inorder(root->right);
    }
}

void preorder(node *root)
{
    if (root)
    {
        printf("%d  ", root->data);
        preorder(root->left);        
        preorder(root->right);
    }
}

void postorder(node *root)
{
    if (root)
    {
        postorder(root->left);        
        postorder(root->right);
        printf("%d  ", root->data);
    }
}

int search(node* root,int key)
{
    int flag=0;
    while(root!=NULL)
    {
        if(root->data==key)
        return 1;
        if(key<root->data)
            root=root->left;
        else if(key>root->data)
            root=root->right;
    }
    return 0;
}

void main()
{
    int ch, val,key;
    node *root = (node *)malloc(sizeof(node));
    root = NULL;
    printf("enter 1 to start creating tree, enter -1 to stop\n");
    scanf("%d", &ch);
    while (ch != -1)
    {
        printf("enter data:");
        scanf("%d", &val);
        root = create_bst(root, val);
        printf("enter choice:");
        scanf("%d", &ch);
    }
    printf("tree created:");
    inorder(root); 

    printf("\nenter key element to search for:");
    scanf("%d",&key);
    if(search(root,key))
    printf("key found");
    else
    {
        root=create_bst(root,key);
        printf("tree after inserting key:");
        printf("\ninorder traversal:\n");
        inorder(root);
        printf("\npreorder traversal:\n");
        preorder(root);
        printf("\npostorder traversal:\n");
        postorder(root);
        exit(0);
    }
    printf("\ntraversals of tree:\n");
    printf("\ninorder traversal:\n");
        inorder(root);
        printf("\npreorder traversal:\n");
        preorder(root);
        printf("\npostorder traversal:\n");
        postorder(root);
}
