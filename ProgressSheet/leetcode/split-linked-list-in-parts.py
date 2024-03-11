# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        temp = head
        count = 0

        while temp:
            temp = temp.next 
            count += 1
        
        ans = []
        leng, extraNode = count // k,  count % k
        temp = head

        for i in range(k):
            ans.append(temp)

            for j in range(leng - 1 + (1 if extraNode else 0)):
                if not temp: break
                temp = temp.next
            
            if extraNode:
                extraNode -= 1
            
            if temp:
                temp.next, temp = None, temp.next

        return ans