class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       # In this approach I am using a two pointers
       # Time complexity: O(n)
       # Space Complexity: O(1)
       replace_index = 0
       for i in range(len(nums)):
        if nums[i] != val:
            nums[replace_index] = nums[i]
            replace_index += 1
       return replace_index

    



        
            

        