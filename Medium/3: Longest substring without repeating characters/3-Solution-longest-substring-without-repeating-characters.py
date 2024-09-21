class Solution:

    def GetFirstOccurance(self, Parameter, ToSearch):
        counter = 0
        for x in ToSearch:
            if x == Parameter:
                return counter
            else:
                counter += 1
        return -1  # Return -1 if not found
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1 = ""
        l2 = ""
        start = 0  # To track the starting point of the current substring
        for i, x in enumerate(s):
            if self.GetFirstOccurance(x, l1) == -1:  # no collision
                l1 = l1 + x
            else:  # collision
                # Adjust the start index based on the collision location
                start = start + self.GetFirstOccurance(x, l1) + 1
                l1 = s[start:i + 1]  # Rebuild the substring without the repeating character

            # Keep track of the longest substring found
            if len(l1) > len(l2):
                l2 = l1
                
        return len(l2)
