class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespaces
        s = s.strip()  
        if len(s) == 0:  # If the string is empty after stripping, return 0
            return 0

        # Step 2: Handle optional sign
        is_positive = True
        i = 0
        if s[0] == '-':
            is_positive = False
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Convert the string to an integer until a non-digit is encountered
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])  # Build the number digit by digit
            i += 1

        # Step 4: Apply the sign
        if not is_positive:
            result = -result

        # Step 5: Clamp the result within the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
