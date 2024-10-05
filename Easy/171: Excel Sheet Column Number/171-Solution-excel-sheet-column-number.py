class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for char in columnTitle:
            total = total * 26 + (ord(char) - ord('A') + 1)
        return total
