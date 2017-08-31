#include <stdio.h>
#include <stdlib.h>

int main(){
    int n=20;
    char a[n];
    scanf("%s", a);
    for (int i = 0; i < 20; i+=3) {
        printf("%c", a[i]);
    }
    for (int i = 1; i < 20; i+=3) {
        printf("%c", a[i]);
    }
    for (int i = 2; i < 20; i+=3) {
        printf("%c", a[i]);
    }
    return 0;
}
