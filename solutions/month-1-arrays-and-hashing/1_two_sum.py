"""
1. Two Sum
-----------------------------------------------------------------------
- Pattern: Hash Map Complement
- How I Recognized It: Brute force nested loops are O(N^2); checking if 
  (target - current_num) exists takes O(1) time using a Hash Map.
- Key Idea: Calculate complement for each number. If complement is in map, 
  return its stored index and current index. Otherwise, store current number:index.
- Time Complexity: O(N)
- Space Complexity: O(N)
-----------------------------------------------------------------------
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}  # Map stores { number_value : index }

        for i in range(len(nums)):
            x = target - nums[i]  # The needed complement
            
            if x in count:
                return [count[x], i]  # Return stored complement's index and current index
            
            count[nums[i]] = i  # Save current number and its index for future steps