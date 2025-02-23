from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       
        # Helper function to calculate the height of the tree and update the diameter
        def height(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter if the path through the current node is longer
            diameter = max(diameter, left_height + right_height)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        # Initialize the diameter to 0
        diameter = 0

        # Start the height calculation from the root
        height(root)

        # Return the calculated diameter
        return diameter

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
    # Input: [1, 2, 3, 4, 5]
    input_list = [1, 2, 3, 4, 5]

    # Convert the list to a binary tree
    root = list_to_tree(input_list)

    # Calculate the diameter of the binary tree
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)

    # Print the result
    print("Input Tree (as list):", input_list)
    print("Diameter of the Tree:", diameter)