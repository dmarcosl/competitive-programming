#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * english_representation(int n) {
    switch (n) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        case 3:
            return "three";
        case 4:
            return "four";
        case 5:
            return "five";
        case 6:
            return "six";
        case 7:
            return "seven";
        case 8:
            return "eight";
        case 9:
            return "nine";
        default:
            return "";
    }
}

char * even_odd(int n) {
    if (n % 2 == 0) {
        return "even";
    } else {
        return "odd";
    }
}

int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);

    for (int i = a; i <= b; i++) {
        if (i <= 9) {
            printf("%s", english_representation(i));
        } else {
            printf("%s", even_odd(i));
        }
        printf("\n");
    }

    return 0;
}

