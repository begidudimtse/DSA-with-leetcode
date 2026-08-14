"""
0347. Top K Frequent Elements
-----------------------------------------------------------------------
- Pattern: Frequency Counter + Map Sorting
- How I Recognized It: We need elements ordered by how often they appear; 
  counting frequencies in a Hash Map and sorting the key-value pairs 
  directly isolates the top K items.
- Key Idea: Count occurrences using a Hash Map, convert to key-value pairs, 
  sort pairs in descending order by frequency, and slice the first K keys.
- Time Complexity: O(N log N) due to sorting unique frequency pairs.
- Space Complexity: O(N) to store frequencies in the dictionary and list.
-----------------------------------------------------------------------
"""

class Solution:
     def topKElements(nums, k):
        count= {}

        for num in nums:
             count[num] = count.get(num,0) + 1

        result = sorted(count.items(), key = lambda x: x[1], reverse = True)

        return [num for num, frequ in result[:k]]