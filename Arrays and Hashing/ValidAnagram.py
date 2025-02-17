class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if the lengths of the strings are different
        if len(s) != len(t):
            return False

        # Initialize dictionaries to store character counts
        count_s = {}
        count_t = {}

        # Iterate through both strings and count character occurrences
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # Compare the two dictionaries
        return count_s == count_t
    

# Example usage
s = "racecar"
t = "carrace"
solution = Solution()
print(solution.isAnagram(s,t))