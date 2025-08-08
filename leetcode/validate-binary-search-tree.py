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
        

        def isValid(root, leftBound, rightBound):
            if root == None:
                return True
            
            if root.val > leftBound and root.val < rightBound:
                return isValid(root.left, leftBound, root.val) and isValid(root.right, root.val, rightBound)
            else:
                return False
        
        return isValid(root, float('-inf'), float('inf'))