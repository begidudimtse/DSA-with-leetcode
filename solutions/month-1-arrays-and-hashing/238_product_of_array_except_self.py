"""
0238. Product of Array Except Self
-----------------------------------------------------------------------
- Pattern: Prefix & Suffix Products (Prefix Decomposition)
- How I Recognized It: O(N) constraint without division means running cumulative 
  products from left and right side must be combined in-place.
- Key Idea: Pass left-to-right to build prefix products in result[], 
  then pass right-to-left multiplying in running suffix products.
- Time Complexity: O(N)
- Space Complexity: O(1) extra space (output array doesn't count towards space).
-----------------------------------------------------------------------
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Calculate prefix products (left of i)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffix products (right of i) and multiply in-place
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result