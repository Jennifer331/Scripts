#include <stdlib.h>
#include <stdio.h>
#include "ch17_p3.h" // queue
#include "ch17_p6.h" // tree

void process(TreeNode *node)
{
    printf("Visited %d\n", node->val);
}

void insertIfNotNull(TreeNode *node)
{
    if (node != NULL) {
        insert(node);
    }
}

void breathFirstTraverse(TreeNode *root, void (*callback)(TreeNode *value))
{
    insert(root);
    while (!isEmpty()) {
        TreeNode *cur = first();
        callback(cur);
        insertIfNotNull(cur->left);
        insertIfNotNull(cur->right);
        delete();
    }
}

void main()
{
    TreeNode *root = &(TreeNode) {.val = 1, .left = NULL, .right = NULL};
    breathFirstTraverse(root, process);
}