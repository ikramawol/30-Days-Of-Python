class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        left = 0
        right = 10**9

        heaters.sort()
        houses.sort()
        def checker(mid):
            l, r = 0, 0
            while l < len(houses) and r < len(heaters):
                if abs(heaters[r] - houses[l]) > mid:
                    r += 1
                else:
                    l += 1
            if r == len(heaters):
                return False
            else:
                return True

        while left <= right:
            mid = (left + right)//2
            if checker(mid) == True:
                right = mid - 1
            else:
                left = mid + 1
        return left               
            