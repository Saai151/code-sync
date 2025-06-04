# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Extract numbers from linked lists
        num1 = 0
        num2 = 0
        
        i = 1
        temp1 = l1
        while temp1:
            num1 += temp1.val * i
            i *= 10
            temp1 = temp1.next
        
        i = 1
        temp2 = l2
        while temp2:
            num2 += temp2.val * i  # Fixed: was adding to num1
            i *= 10
            temp2 = temp2.next
        
        total = num1 + num2
        
        # Handle edge case of 0
        if total == 0:
            return ListNode(0)
        
        # Build result linked list
        dummy = ListNode(0)
        current = dummy
        
        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10
        
        return dummy.next