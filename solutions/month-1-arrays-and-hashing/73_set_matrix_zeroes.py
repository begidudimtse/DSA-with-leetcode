"""

-----------------------------------------------------------------------
- Pattern: In-Place Matrix Marking
- How I Recognized It: Modifying grid values in-place while scanning 
  requires storing state markers in space that won't overwrite unvisited cells.
- Key Idea: Use the 0th row and 0th column as marker arrays, tracking the 
  original state of row 0 and col 0 separately with boolean flags.
- Time Complexity: O(M * N) - Two full passes through the grid.
- Space Complexity: O(1) - Modifies matrix directly in-place.
-----------------------------------------------------------------------
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

       
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

       
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

      
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

    
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0