class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1

        # def helper(mid):
        #     count = 0
        #     for i in range(len(citations)):
        #         if mid >= citations[i]:
        #             count += 1
        #     return count

        while left <= right:
            mid = (left + right)//2

            if citations[mid] == n - mid:
                return citations[mid]

            if citations[mid] > n - mid:
                right = mid - 1
            else:
                left = mid + 1
    
        return  n - left 

