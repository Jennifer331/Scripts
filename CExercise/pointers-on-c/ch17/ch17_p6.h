#define TREE_TYPE int

typedef struct TreeNode {
    TREE_TYPE val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

void breathFirstTraverse(TreeNode *root, void (*callback)(TreeNode *value));