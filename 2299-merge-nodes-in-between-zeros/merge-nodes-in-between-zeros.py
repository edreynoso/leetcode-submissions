# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        ans = ListNode()
        dummy = ans

        curr = head.next

        running_sum = 0

        while curr:

            if curr.val == 0:

                sn = ListNode(running_sum)

                dummy.next = sn
                dummy = dummy.next

                running_sum = 0

            else:
                running_sum += curr.val

            curr = curr.next
        
        return ans.next
