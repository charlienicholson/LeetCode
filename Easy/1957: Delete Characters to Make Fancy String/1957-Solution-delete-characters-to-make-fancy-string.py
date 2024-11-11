class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [] # Fancy str builder
        for char in s:
            # if last two chars in result...
            # if both are same as current then skip
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            # else add char two list
            result.append(char)
        
        # join result to str
        return ''.join(result)
