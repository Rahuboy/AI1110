#include <stdio.h>
#include <math.h>

float income(float nofshares, float divperc, float worth)
{
    return nofshares*divperc*worth;
}

float yieldperc(float income, float cost, float nofshares)
{
    return income/(cost*nofshares)*100;
}

int main()
{
    float nofshares = 90; //number of shares
    float divperc = 0.1; //dividend
    float worth = 50;
    float cost = 60;
    float inc = income(nofshares,divperc,worth);
    printf("income is %f\n",inc);
    printf("yield percentage is %f\n",round(yieldperc(inc,cost,nofshares)));
}
