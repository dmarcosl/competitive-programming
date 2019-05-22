#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char ch, t;
    char s[100], sen[100];

    scanf("%c%s%c%[^\n]", &ch, s, &t, sen);
    printf("%c\n%s\n%s", ch, s, sen);

    return 0;
}

