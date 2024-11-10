class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # This is a bad answer because it might be tailored to the test cases they have
        # And yeah it did not pass
        n = len(nums)
        repl = 0
        counter = 0
        for i in range(0, n-2):
            if nums[i] == val and nums[i+1] != val:
                repl = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = repl
            elif nums[i] == val and nums[i+1] == val:
                repl = nums[i+2]
                nums[i+2] = nums[i]
                nums[i] = repl
        while (nums[counter] != val):
            counter += 1
        return counter
    
    def removeElement(self, nums: List[int], val: int) -> int:
        # initialize and index that points to the position of the next non target element
        # Storing the alamenets that are not val in that index position then moving index forward
        # This has a constant space complexity
        # This has a time complexity of O(n)
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

    



        
            

        