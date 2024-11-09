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
    def removeDuplicates2(self, nums: List[int]) -> int:
        position_index = 1
        
        for i in range (1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[position_index] = nums[i]
                iposition_index = position_index+ 1
        return position_index