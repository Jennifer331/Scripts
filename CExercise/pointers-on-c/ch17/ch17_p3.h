#define QUEUE_TYPE void*

#include <stdlib.h>

typedef struct QueueNode {
    QUEUE_TYPE val;
    struct QueueNode *next;
} QueueNode;

static QueueNode *head = NULL;
static QueueNode *end = NULL;

int isEmpty();

int isFull();

void insert(QUEUE_TYPE value);

void delete();

QUEUE_TYPE first();