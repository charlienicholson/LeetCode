class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold opening brackets
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        # Loop through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in matching_bracket.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in matching_bracket:
                # If stack is empty or the top of the stack doesn't match the corresponding opening bracket, return False
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                # Pop the top of the stack (matched opening bracket)
                stack.pop()
            else:
                # Invalid character
                return False
        
        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0
