# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:  
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        holder = set()
        temp = headA
        curr = headB
        while temp:
            holder.add(temp)
            temp = temp.next

        # print(holder)
        while curr:
            
            if curr in holder:
                return curr
            curr = curr.next