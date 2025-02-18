class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        brackets = {')':'(', ']':'[', '}':'{'}

        # Use a stack to track opening brackets
        stack = []

        # Iterate through each character in the string
        for bracket in s:
            # If the character is a closing bracket
            if bracket in brackets:
                # Check if the stack is not empty and the top of the stack matches the expected opening bracket
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()  # Remove the matched opening bracket from the stack
                else:
                    return False  # If no match, the string is invalid
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(bracket)

        # If the stack is empty, all brackets were properly matched
        return not stack