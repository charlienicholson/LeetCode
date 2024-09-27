class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to track seen elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        return False  # No duplicates found
