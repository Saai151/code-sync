# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = head
        nthNode = head

        length = 0
        while dummy:
            dummy = dummy.next
            length +=1
        
        index = length - n

        dummy = head
        print(index)
        if index == 0:
            return head.next
            
        for i in range(index):
            if i == index - 1:
                temp = dummy.next.next
                dummy.next = temp
            dummy = dummy.next
        
    
        return head