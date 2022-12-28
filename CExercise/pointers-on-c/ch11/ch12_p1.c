#include<stdlib.h>

typedef struct LinkedList {
    struct LinkedList *next;
} LinkedList;

int countNum(LinkedList *l1) {
    int cnt = 0;
    while (l1 != NULL) {
        cnt++;
        l1 = l1 -> next;
    }
    return cnt;
}
