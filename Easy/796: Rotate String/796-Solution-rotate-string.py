class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are the same, as rotation is only possible if lengths match
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself and check if goal is a substring
        return goal in (s + s)
