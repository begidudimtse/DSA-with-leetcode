"""

-----------------------------------------------------------------------
- Pattern: Boyer-Moore Voting Algorithm
- How I Recognized It: Finding an element that appears > n/2 times in 
  O(1) space requires canceling out distinct pairs of elements.
- Key Idea: Maintain candidate and count. Increment count on match, 
  decrement on mismatch. Reset candidate when count hits 0.
- Time Complexity: O(N) - Single pass through nums.
- Space Complexity: O(1) - Constant space.
-----------------------------------------------------------------------
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = 0
        count = 0
        
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
            
        return res