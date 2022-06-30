#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
// uniform("uni.dat", 1000000);

// Gaussian random numbers
// gaussian("gau.dat", 1000000);

//Logarithmic random numbers
// logarithmic("log.dat");

//Mean of uniform
printf("mean = %lf\n",mean("gau.dat"));
printf("variance = %lf",variance("gau.dat"));
return 0;
}


