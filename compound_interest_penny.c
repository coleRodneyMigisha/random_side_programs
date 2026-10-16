#include<stdio.h>

float growPenny() {
    float money, days;
    days=0;
    money=0.1;
    for(days=0; days<=30; days++) {
        money=money*2;
        printf("%.2f on day %.0f \n", money, days);
    }
}

int main() {
    growPenny();

    return 0;
}