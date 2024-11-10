class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This implementaton has:
        # constant space complexity
        # O(log n) runtime complexity

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            mid_value = nums[middle]
            if target == mid_value:
                return middle
            elif target > mid_value:
                left = middle + 1
            else:
                right = middle - 1
        return left