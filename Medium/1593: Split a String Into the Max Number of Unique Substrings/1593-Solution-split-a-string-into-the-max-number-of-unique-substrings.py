class Solution:
    def splitter(self, val: str, checker: set, rep: str) -> int:
        if not val:
            return len(checker)

        max_count = 0
        
        # Try different lengths of substrings starting from the beginning
        for i in range(1, len(val) + 1):
            substring = val[:i]
            if substring not in checker:
                # If the substring is unique, add it to the set and continue
                checker.add(substring)
                max_count = max(max_count, self.splitter(val[i:], checker, ""))
                checker.remove(substring)  # Backtrack

        return max_count

    def maxUniqueSplit(self, s: str) -> int:
        return self.splitter(s, set(), "")
