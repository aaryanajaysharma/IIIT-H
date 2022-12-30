#include<stdio.h>

int main()
{
    char a[] = "hello";
    int sum = 0;
    int i;
    for(i = 0; i < 5; i++)
    {
        sum += (a[i]-'a');
    }
    printf("%d\n", sum);
    return 0;
}