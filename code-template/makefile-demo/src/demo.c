#include "demo.h"
#include "sum.h"

int main(int argc, char *argv[])
{
        PRINTF("argc:%d\r\n", argc);
        for (int i = 0; i < argc; ++i)
                PRINTF("argv[%d]:%s\r\n", i, argv[i]);

        if (argc > 2) {
                int a = atoi(argv[1]);
                int b = atoi(argv[2]);
                int s;
                sum(&s, a, b);
                PRINTF("a:%d b:%d sum:%d\r\n", a, b, s);
        }

        return 0;
}
