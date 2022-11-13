#include "sum_impl.h"
#include "sum.h"

void sum(int *sum_ptr, int a, int b)
{
        if (!sum_ptr)
                return;

        *sum_ptr = a + b;
}
