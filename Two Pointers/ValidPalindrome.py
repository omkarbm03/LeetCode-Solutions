class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize pointers at the start and end of the string

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric characters from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False  # Not a palindrome if characters don't match
            l, r = l + 1, r - 1  # Move pointers towards the center
        return True  # String is a palindrome if all characters matched
    
    # Helper function to check if a character is alphanumeric
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

#Example Usage     
solution = Solution()
s = "Was it a car or a cat I saw?"
print(solution.isPalindrome(s))
