class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = Counter(nums)
        
        _max = max(majority.values())
        
        keys = [key for key, val in majority.items() if val ==_max]
        
        return keys[0]
            
        
        