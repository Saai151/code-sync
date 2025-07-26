# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        q = collections.deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr:
                heapq.heappush(heap, curr.val)
                q.append(curr.left)
                q.append(curr.right)
        val = 0
        for i in range(k):
            val = heapq.heappop(heap)
        
        return val