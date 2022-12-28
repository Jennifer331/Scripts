#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include "ch17_p3.h"

int isEmpty()
{
    return head == NULL;
}

int isFull()
{
    return 0;
}

void insert(QUEUE_TYPE value)
{
    QueueNode *n = malloc(sizeof(QueueNode));
    n->val = value;
    n->next = NULL;
    if (head == NULL) {
        head = n;
    } else {
        end -> next = n;
    }
    end = n;
}

void delete()
{
    assert(!isEmpty());
    QueueNode *tmp = head;
    head = head->next;
    free(tmp);
}

QUEUE_TYPE first()
{
    assert(!isEmpty());
    return head->val;
}
