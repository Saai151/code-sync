# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = []
        heapq.heapify(res)
        

        for l in lists:
            curr = l
            while(curr):
                heapq.heappush(res, curr.val)
                curr = curr.next
        print(res)

        ans = ListNode()
        mover = ans
        while res:
            val = heapq.heappop(res)
            mover.next = ListNode(val)
            mover = mover.next
        return ans.next