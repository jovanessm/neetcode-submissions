# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_depth = 1
        def searchDepth(node, depth):
            self.max_depth = max(self.max_depth, depth)
            if node:
                if node.left:
                    searchDepth(node.left, depth + 1)
                if node.right:
                    searchDepth(node.right, depth + 1)
        searchDepth(root, self.max_depth)
        return self.max_depth
