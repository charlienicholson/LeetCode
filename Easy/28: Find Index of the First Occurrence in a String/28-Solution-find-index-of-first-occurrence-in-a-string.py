class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: #empty needle
            return 0
        if len(needle) > len(haystack): #needle > haystack
            return -1
        #iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):  #stay in bounds
            #check if the substring matches the needle
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                else: #didn't break
                    return i
                
        return -1
