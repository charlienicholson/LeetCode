class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Pad the shorter string with leading zeros
        a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))
        
        carry = 0
        result = []
        
        # Iterate from the last digit to the first
        for i in range(len(a) - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry  # Binary addition
            carry = total // 2                    # Determine new carry (1 or 0)
            result.append(str(total % 2))         # Append the sum mod 2 to result
        
        # If there's a remaining carry, add it
        if carry:
            result.append("1")
        
        # Join the list and reverse to get the final result
        return ''.join(result[::-1])
