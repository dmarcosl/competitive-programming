#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);

    int numbers[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            int n = (int)s[i] - 48;
            numbers[n] = numbers[n] + 1;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}

