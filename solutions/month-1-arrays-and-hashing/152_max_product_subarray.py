"""
-----------------------------------------------------------------------
- Pattern: Dynamic Programming / Modified Kadane's (Max & Min Tracking)
- How I Recognized It: Continuous subarray products depend on sign flips; 
  a negative number flips a minimum product into a maximum product.
- Key Idea: Maintain both running `cur_max` and `cur_min`. At a negative 
  number, swap them before computing new max/min values.
- Time Complexity: O(N) - Single pass through nums.
- Space Complexity: O(1) - Uses constant extra memory.
-----------------------------------------------------------------------
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_max = 1
        cur_min = 1
        
        for num in nums:
            tmp_max = cur_max * num
            
            cur_max = max(num, tmp_max, cur_min * num)
            cur_min = min(num, tmp_max, cur_min * num)
            
            res = max(res, cur_max)
            
        return res