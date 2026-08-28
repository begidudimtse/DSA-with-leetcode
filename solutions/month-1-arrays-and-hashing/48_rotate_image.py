"""
-----------------------------------------------------------------------
- Pattern: Matrix Manipulation (Transpose + Reverse)
- How I Recognized It: 90-degree clockwise rotation in-place is mathematically 
  equivalent to reflecting along the main diagonal (transpose) and then 
  reflecting horizontally (reversing rows).
- Key Idea: Transpose matrix in-place using upper triangle indices (j > i), 
  then reverse each row in-place.
- Time Complexity: O(N^2) - N x N matrix traversal.
- Space Complexity: O(1) - In-place modification.
-----------------------------------------------------------------------
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 1. Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. Reverse each row
        for i in range(n):
            matrix[i].reverse()