class Solution:

    def strToList(self, strToConvert: str) -> List[str]:
        wordList = []
        word = ""
        for x in strToConvert:
            if x.isalpha():
                word += x
            else: #if not a letter then a space " "
                wordList.append(word)
                word = ""
        wordList.append(word)#adds last word of sentance
        return wordList
      
    def removeDuplicates(self, lX: List[str]) -> List[str]:
        counts = {}
        for item in lX:
            counts[item] = counts.get(item, 0) + 1 #add item to dict and increase val
        return [item for item in lX if counts[item] == 1] #dict val occurs 1'ce
      
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = self.strToList(s1) #to list
        l2 = self.strToList(s2) # ''
        for x in l2:
            l1.append(x) #merge list
        l1 = self.removeDuplicates(l1) #remove dupes
        return l1
