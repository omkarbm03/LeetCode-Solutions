class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      

        start = 0 
        max_len = 0 
        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i],0)

            while counts[s[i]] > 1:
                counts[s[start]] -= 1 
                start += 1 

            max_len = max(max_len,i-start+1)

        return max_len


solution = Solution()
s = "zxyzxyz"
print(solution.lengthOfLongestSubstring(s))
