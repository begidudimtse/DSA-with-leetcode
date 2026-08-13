"""
0049. Group Anagrams
-----------------------------------------------------------------------
- Pattern: Hash Map Categorization / String Canonicalization
- How I Recognized It: Comparing all word pairs takes O(N^2); 
  transforming words into a single sorted signature allows grouping in O(1) time.
- Key Idea: Use the sorted character string as a dictionary key to group 
  matching original words in a list.
- Time Complexity: O(N * K log K) where N = len(strs) and K = max word length.
- Space Complexity: O(N * K) to store grouped string lists in the dictionary.
-----------------------------------------------------------------------
"""

class Solution:
    def groupAnagrams(self, strs):
        result = {}  # Map stores { sorted_word : list_of_anagrams }

        for word in strs:
            key = ''.join(sorted(word)) 
            
            if key not in strs:
                result[key] = []  
            
            result[key].append(word)  

        return list(result.values()) 