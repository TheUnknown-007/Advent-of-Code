#include <stdio.h>

void main()
{
    char main[100];
    FILE* fptr = fopen("Test.txt", "r");
    fgets(main, 100, fptr);
    //printf("%c". main[0]);
}