#ifndef __DEMO_H__
#define __DEMO_H__

#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdlib.h>

#define PRINTF(fmt, args...)  \
        do { printf("[%s %d] " fmt, __FILE__, __LINE__, ##args); } while(0)

#ifdef __cplusplus
}
#endif

#endif // !__DEMO_H__
