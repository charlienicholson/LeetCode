class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLetters = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                sLetters+=char.lower()
        return sLetters == sLetters[::-1]
