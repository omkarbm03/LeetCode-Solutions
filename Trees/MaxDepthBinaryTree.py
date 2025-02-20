from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        # Base case: if the root is None, the depth is 0
        if not root:
            return 0

        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum depth of the two subtrees, plus 1 for the current node
        return 1 + max(left_depth, right_depth)

# Helper function to create a binary tree from a list (for testing)
def list_to_tree(lst: list, index: int = 0) -> Optional[TreeNode]:
   
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = list_to_tree(lst, 2 * index + 1)  # Left child
    root.right = list_to_tree(lst, 2 * index + 2)  # Right child
    return root

# Example Usage
if __name__ == "__main__":
    # Input: [3, 9, 20, None, None, 15, 7]
    input_list = [3, 9, 20, None, None, 15, 7]

    # Convert the list to a binary tree
    root = list_to_tree(input_list)

    # Calculate the maximum depth of the binary tree
    solution = Solution()
    max_depth = solution.maxDepth(root)

    # Print the result
    print("Input Tree (as list):", input_list)
    print("Maximum Depth of the Tree:", max_depth)