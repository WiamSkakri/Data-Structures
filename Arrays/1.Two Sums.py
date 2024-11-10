class Solution:
    # This solution has O(n^2) time complexity
    # Constant space complexity
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:

                    return i, j
                
    # This is a hash table approach (2 way)
    # This has both a space complexity and time complexity of O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        
        # Creating the hash table
        for i in range (n):
            numMap[nums[i]] = i
        
        # Finding the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return[]