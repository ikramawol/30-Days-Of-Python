class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        def validator(capacity):
            _sum = 0

            for i in range(len(piles)):
                _sum += ceil(piles[i]/capacity)
            return _sum
            
        while left <= right:
            mid = (left + right)//2
            d = validator(mid)
            if d > h:
                left = mid + 1
            else:
                right = mid - 1
            
        return left