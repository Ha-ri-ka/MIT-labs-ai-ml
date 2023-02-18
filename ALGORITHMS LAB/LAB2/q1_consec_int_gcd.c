#include<stdio.h>
int greatest_common_divisor(int m,int n)
{
    int t=m>n?n:m;
    int Cop=0;
    while(t!=0)
    {
        Cop++;
        if(m%t==0)       
        {
            if(n%t==0)
            {
                printf("operation count is %d\n",Cop);
                return t;
            }
            else
            t=t-1;          
        }
        else
        t-=1;
    }
    return -1;
}

void main()
{
    int m,n,gcd;
    printf("enter the numbers you'd like to know the gcd of\n");
    jump:
    printf("m="); scanf("%d",&m); printf("n="); scanf("%d",&n);
    if(m<0||n<0||(m==0&&n==0)) 
    {
        printf("invalid inputs. please enter again:");
        goto jump;
    }
    gcd=greatest_common_divisor(m,n);
    if(gcd!=-1)
    printf("the greatest common divisor of given numbers is:%d",gcd);
    else
    printf("the greatest common divisor of given numbers is:%d",((m==0)?n:m));
}
