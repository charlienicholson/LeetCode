class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        errorvals = {"AB", "CD"}

        for char in s:
            if stack:  # Ensure stack is not empty
                selection = stack[-1] + char
                if selection in errorvals:  # If the pair is "AB" or "CD"
                    stack.pop()
                    continue  # Skip appending this character
            stack.append(char)  

        return len(stack) 
