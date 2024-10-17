class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the sorted left side
                else:
                    left = mid + 1   # Target is in the right part
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the sorted right side
                else:
                    right = mid - 1  # Target is in the left part

        return -1  # Target not found
