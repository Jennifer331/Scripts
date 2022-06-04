#include<stdio.h>

struct BBB {
    long INum;
    char *pcName;
    short sDate;
    char cHa[2];
    short sBa[6];
} *p;

void exercise1() {
    printf("size of long: %d\n", sizeof(long));
    printf("p: %d, sizeof BBB: %d\n", p, sizeof(struct BBB));
    printf("p + 0x1: %d\n", p + 0x1);
    // printf("(unsigned long)p: %lu\n", (unsigned long)p);
    printf("(unsigned long)p + 0x1: %lu\n", (unsigned long)p + 0x1);
    printf("(unsigned long *)p + 0x1: %lu\n", (unsigned long *)p + 0x1);
    printf("(char *)p + 0x1: %d", (char *)p + 0x1);
}

void exercise2() {
    int *p;
    for (int i = 0; i < 10; i++) {
        p = &i;
    }
    printf("*p: %d, p: %d", *p, p);
}

struct tagSmart {
    char flag1;
    int (*left_tree)[3];
    struct tagSmart *right_tree[2];
    char flag3;
    char flag4;
} SmartFlag[4];

void exercise5() {
    printf("sizeof char: %d\n", sizeof(char));
    printf("sizeof tagSmart: %d\n", sizeof(struct tagSmart));
    printf("sizeof tagSmart*: %d\n", sizeof(struct tagSmart*));
    printf("sizeof SmartFlag: %d\n", sizeof(SmartFlag));
}

void exercise6() {
    char acNew[] = "Welcome\0To\0Huawei\0";
    printf("sizeof: %d, strlen: %d", sizeof(acNew), strlen(acNew));
}

void exercise7() {
    char x = 0xFFFE;
    printf("%d\n", x);
    int y = -2;
    printf("%x\n", y);
}

void exercise9() {
    int a[3][3], *p, i;
    p = &a[0][0];
    for (int i = 0; i < 9; i++) {
        p[i] = i + 1;
    }

    for (int i = 0; i < 3; i++) {
        printf("%d, %d, %d\n", a[i][0], a[i][1], a[i][2]);
    }
}

void exercise10() {
    int x = 10;
    char *p = &x;
    printf("p: %d\n", p);
    printf("p + 1: %d\n", p + 1);
    // printf("((int*)p)++: %d\n", ((int*)p)++);//((int*)p)++ 表达式必须是可修改的左值错误
    printf("p += sizeof(int): %d\n", p + sizeof(int));
}

typedef struct {
    int a[5];
} Foo1;

typedef struct {
    int (*a)[5];
    char b;
} Foo2;

typedef struct {
    int (*a)[5];
} Foo3;

typedef struct {
    int *a[2];
    char b;
} Foo4;

typedef struct {
    int (*a[5])();
} Foo5;

void exercise11() {
    printf("sizeof(Foo1): %d\n", sizeof(Foo1));
    printf("sizeof(Foo2): %d\n", sizeof(Foo2));
    printf("sizeof(Foo3): %d\n", sizeof(Foo3));
    printf("sizeof(Foo4): %d\n", sizeof(Foo4));
    printf("sizeof(Foo5): %d\n", sizeof(Foo5));
    printf("sizeof(char): %d\n", sizeof(char));
}

void exercise12() {
    union {
        long k;
        char i[2];
    } *s, a;
    s = &a;
    s -> i[0] = 0x39;
    s -> i[1] = 0x38;
    printf("%x\n", a.k);
    printf("sizeof(s): %d, sizeof(a): %d\n", sizeof(s), sizeof(a));
}

void exercise13() {
    unsigned int a = 20;
    int b = 13;
    int k = b - a;
    printf("k: %d\n", b, k);
    if (k < (unsigned int)b + a)
        printf("(unsigned int)b + a: %u\n", (unsigned int)b + a);
    if (k < b + (int)a)
        printf("b + (int)a: %u\n", b + (int)a);
    if (k < (int)(b + a))
        printf("(int)(b + a): %u\n", (int)(b + a));
    if (k > b + a)
        printf("b + a: %u\n", b + a);
    printf("done!");
}

void exercise14() {
    int x = 0;
    int y = 0;
    // int const * const z = &x;//导致z = &y报错：表达式必须是可修改的左值C/C++(137)
    const int const *z = &x;// ok
    // int const *z = &x;// ok
    // int * const z = &x;////导致z = &y报错：表达式必须是可修改的左值C/C++(137)
    z = &y;
}

char *GetMemory1(void) {
    char *p = "hello world";
    return p;
}

char *GetMemory2(void) {
    char p[] = "hello world";
    return p;
}

char *GetMemory3(void) {
    static char p[] = "hello world";
    return p;
}

char *GetMemory4(void) {
    char *p = malloc(100);
    memset(p, 0, 100);
    strncpy(p, "hello world", strlen("hello world"));
    return p;
}

void exercise15() {
    char *buf = NULL;
    buf = GetMemory1();
    printf("GetMemory1: %s\n", buf);
    buf = GetMemory2();
    printf("GetMemory2: %s\n", buf);
    buf = GetMemory3();
    printf("GetMemory3: %s\n", buf);
    buf = GetMemory4();
    printf("GetMemory4: %s\n", buf);
}

int main() {
    // exercise13();
    printf("-7: %u", -7);
    return 0;
}