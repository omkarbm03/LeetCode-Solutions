from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()  # Use a set for O(1) lookups

        for num in nums:
            if num in visited:  # Check if the number is already in the set
                return True
            visited.add(num)  # Add the current number to the set

        return False  # No duplicates found

# Example usage
nums = [1, 2, 3, 4, 5, 5, 3, 1]
solution = Solution()
print(solution.hasDuplicate(nums))  