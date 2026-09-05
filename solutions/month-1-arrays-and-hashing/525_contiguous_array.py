"""

-----------------------------------------------------------------------
- Pattern: Count Difference Tracking (ones - zeros)
- Key Idea: Maintain separate counts for 0s and 1s. When (ones - zeros) 
  repeats, the subarray between the two occurrences has equal 0s and 1s.
- Time Complexity: O(N)
- Space Complexity: O(N)
-----------------------------------------------------------------------
"""

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # Notebook stores: {difference: earliest_index}
        seen = {0: -1}
        
        zeros = 0
        ones = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
                
            diff = ones - zeros
            
            if diff in seen:
                max_len = max(max_len, i - seen[diff])
            else:
                seen[diff] = i
                
        return max_len