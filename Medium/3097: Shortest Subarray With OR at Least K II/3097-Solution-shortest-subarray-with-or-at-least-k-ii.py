class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
       
        min_length = float('inf')  # Start with a large number for minimum length

        for start in range(len(nums)):
            current_or = 0  # Reset OR for each new starting position
            
            for end in range(start, len(nums)):
                current_or |= nums[end]  # Update the OR value by including nums[end]
                
                # Check if the current subarray meets the requirement
                if current_or >= k:
                    min_length = min(min_length, end - start + 1)  # Update minimum length
                    break  # No need to expand further, go to next starting point

        return min_length if min_length != float('inf') else -1
 
