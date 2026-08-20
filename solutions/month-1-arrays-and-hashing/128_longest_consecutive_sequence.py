"""
0128. Longest Consecutive Sequence
-----------------------------------------------------------------------
- Pattern: Hash Set Sequence Building
- How I Recognized It: Sorting takes O(N log N); using a Hash Set allows 
  O(1) existence checks to identify sequence starting points.
- Key Idea: Only count sequences starting from numbers where (num - 1) 
  is not in the set.
- Time Complexity: O(N)
- Space Complexity: O(N)
-----------------------------------------------------------------------
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count consecutive numbers
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest