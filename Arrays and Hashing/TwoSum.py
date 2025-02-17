from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary to store the difference between the target and each number
        num_to_index = {}

        # Iterate through the list with index and value
        for index, num in enumerate(nums):
            
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                
                return [num_to_index[complement], index]

            # Store the current number and its index in the dictionary
            num_to_index[num] = index

        

solution = Solution()
target = 7 
nums = [2,3,5,6,7,4]
print(solution.twoSum(nums,target))