class Solution:
    # Binary Search method to determine if a target exists in the sorted array
    def binarySearch(self, arr: List[int], target: int, low: int, high: int) -> bool:
        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid index
            
            if arr[mid] == target:
                return True  # Target found
            elif arr[mid] < target:  # Target is larger, move to the right half
                low = mid + 1
            else:  # Target is smaller, move to the left half
                high = mid - 1
        return False  # Target not found

    # Method to find the longest sequence where each element is a square of the previous
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()  # Sort array to ensure ordered traversal
        maxSquares = 0  # Track the maximum length of square streak
        partOfSequence = set()  # Track numbers already part of a square sequence

        for current in nums:
            if current in partOfSequence:
                continue  # Skip numbers that are already part of a sequence

            squared = current ** 2  # Square of current number
            sequenceLength = 1  # Initialize sequence length with current element
            
            while True:
                # Check if the squared value exists in nums using binary search
                if self.binarySearch(nums, squared, 0, len(nums) - 1):
                    partOfSequence.add(squared)  # Mark squared as part of sequence
                    sequenceLength += 1  # Increment sequence length
                    squared = squared ** 2  # Square the number for next check
                else:
                    break  # End loop if squared is not found in nums

            # Update maxSquares if the current sequence is the longest found
            maxSquares = max(maxSquares, sequenceLength) if sequenceLength > 1 else maxSquares

        return maxSquares if maxSquares >= 2 else -1  # Return -1 if no valid streak found
