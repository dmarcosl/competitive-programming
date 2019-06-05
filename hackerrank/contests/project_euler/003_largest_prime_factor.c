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
        long prime = 1;

        while(n % 2 == 0) {
            prime = 2;
            n /= 2;
        }

        for (int i = 3; i <= sqrt(n); i += 2) {
            while (n % i == 0) {
                prime = i;
                n = n / i;
            }
        }

        if (n > 2) {
            prime = n;
        }
        
        printf("%ld\n", prime);
    }
    return 0;
}

