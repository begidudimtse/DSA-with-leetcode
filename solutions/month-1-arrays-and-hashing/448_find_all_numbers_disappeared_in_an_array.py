"""
-----------------------------------------------------------------------
- Pattern: Hash Set Lookup
- How I Recognized It: Checking presence/absence across range [1, n].
- Time Complexity: O(N) - Creating set takes O(N), loop 1..N takes O(N).
- Space Complexity: O(N) - Stores up to N unique elements in set.
-----------------------------------------------------------------------
"""

class SolutionHashSet:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # 1. Convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # 2. Collect numbers from 1 to n that are not in the set
        res = []
        n = len(nums)
        
        for number in range(1, n + 1):
            if number not in num_set:
                res.append(number)
                
        return res