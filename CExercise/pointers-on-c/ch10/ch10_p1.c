#include <stdlib.h>

typedef struct {
    short areaCode;
    short exchange;
    short station;
} PHONE_NUM;

typedef struct {
    short month;
    short day;
    short year;
    int time;
    PHONE_NUM called;
    PHONE_NUM calling;
    PHONE_NUM billed;
} BILLING;