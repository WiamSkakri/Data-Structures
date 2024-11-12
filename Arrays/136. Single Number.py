class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # This is a brute force solution
        # Space complexit: O(n)
        # Time complexity: O(n^2)
        # That is because we iterate through nums and then do the search operation inside the for loop
        single = []
        for i in nums:
            if i not in single:
                single.append(i)
            else:
                single.remove(i)
        return single.pop()
    
    def singleNumber(self, nums: List[int]) -> int:
        # Space complexity: O(n)
        # Time complexity: O(n) since we do not have to do the search operation using the hash table
        # The hash table relate each value to the number of its occurences
         hash_table = defaultdict(int)
        for i in nums: 
            # increase the i each time we pass that same number
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i
            
    def singleNumber(self, nums: List[int]) -> int:
        # This apprach uses math: 2∗(a+b+c)−(a+a+b+b+c)=c
        # it is useful to know that: sum(set(nums)) = the sum of elements occuring once in the list
        # sum(nums) sums all element and duplicates
        # Time complexity: O(n + n) -> n
        # Space complexity: O(n + n) -> n
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber(self, nums: List[int]) -> int:
        # using xor
        # a⊕0=a
        # a⊕a=0
        # so: a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # Space complexity: Constant
        # Time complexity: O(n) since we only iterate through nums
        a = 0
        for i in nums:
            a ^= i
        return a
    

    