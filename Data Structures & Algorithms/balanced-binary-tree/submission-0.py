# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def getDepth(node):
            nonlocal isBalanced
            if not node:
                return 0
            left_depth = getDepth(node.left)
            right_depth = getDepth(node.right)
            heightDiff = right_depth - left_depth
            if heightDiff < -1 or heightDiff > 1:
                isBalanced = False
            return max(left_depth, right_depth) + 1
        getDepth(root)
        return isBalanced