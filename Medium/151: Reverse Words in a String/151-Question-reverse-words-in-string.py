class Solution:

    def strToList(self, string: str) -> List[str]:
        strList = []
        word = []
        for x in string:
            if x.isalpha() or x.isnumeric():
                word.append(x)
            else:
                if word:
                    strList.append("".join(word))
                    word = []
        if word:
            strList.append("".join(word))
        return strList

    def reverseWords(self, s: str) -> str:
        sList = self.strToList(s)
        sList.reverse()  # reverse in place without reassignment
        s = " ".join(sList).strip()  # strip leading/trailing spaces in one go
        return s
