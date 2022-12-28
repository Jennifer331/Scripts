#include<singly_linked_list_node.h>
#include <stdlib.h>

int sll_remove(struct Node **rootp, struct NODE *delete) {
    struct Node *cur;
    struct Node **curp = rootp;
    while ((cur = *curp) != NULL && cur != delete)
        curp = &cur->next;

    if (cur == delete) {
        *curp = *curp->next;
        free(delete);
        return true;
    }
    return false;
}