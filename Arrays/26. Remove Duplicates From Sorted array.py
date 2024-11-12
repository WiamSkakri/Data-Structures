class Solution:
   # The required return is so confusing in here

    # Using the set because it automatically removes duplicates
    def removeDuplicates1(self, nums: List[int]) -> int:
          s = set(nums)
          nums.clear()
          for i in s:
               nums.append(i)
          return len(nums)
    
    # using two pointers
    # In this approach we have a:
        # Space complexity: O(1)
        # Time complexity: O(n)
    def removeDuplicates2(self, nums: List[int]) -> int:
        position_index = 1
        
        for i in range (1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[position_index] = nums[i]
                position_index = position_index+ 1
        return position_index
    
    