# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        left = root.left
        right = root.right

        def isValid(root, leftBound, rightBound):
            if root == None:
                return True
            left = root.left
            right = root.right
            if root.val > leftBound and root.val < rightBound:
                return isValid(left, leftBound, root.val ) and isValid(right, root.val, rightBound)
            else:
                return False
        
        return isValid(left, float('-inf'), root.val) and isValid(right, root.val, float('inf'))