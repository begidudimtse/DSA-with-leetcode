"""

-----------------------------------------------------------------------
- Pattern: Prefix Sum + Hash Map Frequency Counter
- How I Recognized It: Finding continuous subarrays summing to K with negative 
  numbers allowed (where sliding window fails) requires checking running prefix sums.
- Key Idea: If current_sum - prefix_sum = k, then a valid subarray exists. 
  Map stores {prefix_sum: frequency}.
- Time Complexity: O(N) - Single pass through nums.
- Space Complexity: O(N) - Hash map stores up to N prefix sums.
-----------------------------------------------------------------------
"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_counts = {0: 1}  # Base case for subarrays starting at index 0

        for num in nums:
            current_sum += num
            
            # Check if a complement prefix sum exists that makes a subarray of sum k
            diff = current_sum - k
            if diff in prefix_counts:
                count += prefix_counts[diff]
                
            # Record current prefix sum
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return count




        