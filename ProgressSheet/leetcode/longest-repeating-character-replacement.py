class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)
        max_count, max_len = 0,0
        l = 0 

        for r in range(len(s)):
            counter[s[r]] += 1

            max_count = max(max_count, counter[s[r]])

            if max_len - max_count >= k:
                counter[s[r - max_len]] -= 1
                # l += 1
            else:
                max_len += 1
            # max_len = max(max_len, r - l + 1)

        return max_len
            
