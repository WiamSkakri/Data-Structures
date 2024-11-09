class Solution(object):
    # This solution has an O(n^2)
    # def containsDuplicate(self, nums):
    #     for i in range (len(nums)):
    #         for j in range (i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False
    
    # Let us try to make it
    #  Time Complexity: O(n)
    # Space Complexity: O(n)
    # def containsDuplicate(seld, nums):
    #     past = list()
    #     for num in nums:
    #         if num in past:
    #             return True
    #         past.append(num)
    #     return False
    

    # Let us use sorting
    # Time complexity: O(nlogn)
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False



