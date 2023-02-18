#include<stdio.h>
int euclids_greatest_common_divisor(int m,int n)
{
    static int Cop=0;
    if(n==0)
    {
        printf("operation count is %d\n",Cop);
        return m;
    }
    Cop+=1; 
    return euclids_greatest_common_divisor(n,m%n);        
}

void main()
{
    int m,n,gcd;
    printf("enter the numbers you'd like to know the gcd of\n");
    jump:
   { printf("m="); scanf("%d",&m); printf("n="); scanf("%d",&n);}
    if(m<0||n<0||(m==0&&n==0)) 
    {
        printf("invalid inputs. please enter again:");
        goto jump;
    }
    gcd=euclids_greatest_common_divisor(m,n);
    printf("the greatest common divisor of given numbers is:%d",gcd);
}
