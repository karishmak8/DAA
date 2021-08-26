#include<stdio.h>
void main()
{
    int n,i,s;
    printf("enter the size of the array:");
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements of the list:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter search element:");
    scanf("%d",&s);
    for(i=0;i<n;i++)
    {
        if(arr[i]==s)
        {
        printf("search element found at index %d",i);
        return;
        }
        if(i==n-1)
        {
            printf("search element not found\n");
        }
    }
}
