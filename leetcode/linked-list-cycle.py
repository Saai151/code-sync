# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()

        dummy = head
        while dummy:
            if dummy in visited:
                return True
            else:
                visited.add(dummy)
                dummy = dummy.next
        return False