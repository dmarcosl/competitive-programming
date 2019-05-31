#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long n; 
        scanf("%ld",&n);
        long sum = 0;
        long prev = 0;
        long prev2 = 1;
        for (long j = 1; j < n; j+=prev) {
            prev = prev2;
            prev2 = j;

            if (j % 2 == 0) {
                sum += j;
            }
        }
        printf("%ld\n", sum);
    }
    return 0;
}

