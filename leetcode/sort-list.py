# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = []

        dummy = head
        while(dummy):
            res.append(dummy.val)
            dummy = dummy.next

        res.sort()

        if not res:
            return head
            
        output = ListNode(res[0])
        dummy = output

        for i in range(1, len(res)):
            dummy.next = ListNode(res[i])
            dummy = dummy.next
        
        return output