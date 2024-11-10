class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Time complexity is O(m + n)
        # Space complexity is O(1)
        nidx = n - 1
        midx = m - 1
        end = m + n - 1
        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[end] = nums1[midx]
                midx -= 1
            else :
                nums1[end] = nums2[nidx]
                nidx -= 1
            end -= 1
