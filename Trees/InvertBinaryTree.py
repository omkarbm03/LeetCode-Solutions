from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree recursively.
        
        Args:
            root (Optional[TreeNode]): The root of the binary tree.
        
        Returns:
            Optional[TreeNode]: The root of the inverted binary tree.
        """
        # Base case: if the root is None, return None
        if not root:
            return None

        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root

# Helper function to create a binary tree from a list (for testing)
def list_to_tree(lst: list, index: int = 0) -> Optional[TreeNode]:
    """
    Converts a list representation of a binary tree into a TreeNode structure.
    
    Args:
        lst (list): The list representation of the binary tree.
        index (int): The current index in the list.
    
    Returns:
        Optional[TreeNode]: The root of the binary tree.
    """
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = list_to_tree(lst, 2 * index + 1)  # Left child
    root.right = list_to_tree(lst, 2 * index + 2)  # Right child
    return root

# Helper function to convert a binary tree back to a list (for visualization)
def tree_to_list(root: Optional[TreeNode]) -> list:
    """
    Converts a binary tree into a list representation.
    
    Args:
        root (Optional[TreeNode]): The root of the binary tree.
    
    Returns:
        list: The list representation of the binary tree.
    """
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example Usage
if __name__ == "__main__":
    # Input: [4, 2, 7, 1, 3, 6, 9]
    input_list = [4, 2, 7, 1, 3, 6, 9]

    # Convert the list to a binary tree
    root = list_to_tree(input_list)

    # Invert the binary tree
    solution = Solution()
    inverted_root = solution.invertTree(root)

    # Convert the inverted tree back to a list for visualization
    inverted_list = tree_to_list(inverted_root)

    # Print the result
    print("Original Tree (as list):", input_list)
    print("Inverted Tree (as list):", inverted_list)