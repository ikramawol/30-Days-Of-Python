class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        ans = []
        candles = []
        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)
        # print(ca/ndles)

        for l,r in queries:
            if s[l] == '|':
                left = bisect_left(candles, l)
            else:
                left = bisect_right(candles, l)
            
            right = bisect_left(candles, r) 

            if s[r] != '|':
                right -= 1

            # if right < len(candles) and candles[right] == r:
            #     pass
            # else:
            #     right -= 1

            # print(l,r)
            # print(left, right)
            # print(candles[left], candles[right])

            if left >= right:
                ans.append(0)
                continue

            # print("#", candles[right],  candles[left])
            res = (candles[right] - candles[left] + 1) - (right - left + 1)
            ans.append(res)
        return ans 

            
