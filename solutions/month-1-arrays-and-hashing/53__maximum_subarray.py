"""
0053. Maximum Subarray
-----------------------------------------------------------------------
- Pattern: Dynamic Programming / Kadane's Algorithm
- How I Recognized It: Finding contiguous subarray maximums in O(N) time 
  requires deciding at each index whether to extend the previous sequence 
  or start a new one.
- Key Idea: Maintain running total `current_sum`. If it drops below 0, 
  reset it to 0. Update `max_sum` at each step.
- Time Complexity: O(N) - Single pass through nums.
- Space Complexity: O(1) - Uses only two integer variables.
-----------------------------------------------------------------------
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # Add current number to running total
            current_sum += num
            
            # Update max_sum if current_sum beats it
            max_sum = max(max_sum, current_sum)
            
            # If current_sum becomes negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
                
        return max_sum


