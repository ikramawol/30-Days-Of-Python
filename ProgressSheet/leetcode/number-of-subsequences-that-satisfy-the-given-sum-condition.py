class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            max_num = target - nums[i]
            idx = bisect_right(nums, max_num, i + 1)
               
            if nums[i] + nums[idx-1] <= target:
                ans += (2**(idx - i - 1)) % mod
            else:
                break
                
        return ans % mod