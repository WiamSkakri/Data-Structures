class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # This implementation has a constant space complexity  
        # This implementation has a run time complexity of O(n)
       
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else :
                digits[i] = 0
        return [1] + digits