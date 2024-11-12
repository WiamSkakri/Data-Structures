class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # This approach appends nums to the resulted array twice
        # Time complexity: O(N)
        # Space complexity: O(1)
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result

# Making the code generic for any number of times
    def getConcatenation(self, nums: List[int]) -> List[int]:
            ans = []
            # change the 2 if 
            for i in range(2):
                for n in nums:
                     ans.append(n)
            return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Creating a new list of size 2n
        # Time complexity: O(n)
        # Space complexity: O(n)
        results = [0] * (2 * n)
        for i in range(n):
            # copying the first half
            results[i] = nums[i]
            # copying the second hald
            results[i + n] = nums[i]
        return results

    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Extend the list with itself
        # Time complexity: O(n)
        # Space complexity: O(n)
        nums.extend(nums)
        return nums

    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Concatenate the list with itself
        # Time complexity: O(n)
        # Space complexity: O(n)
        return nums + nums

    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Repeat the list twive
        # Time complexity: O(n)
        # Space complexity: O(n)
        return nums * 2