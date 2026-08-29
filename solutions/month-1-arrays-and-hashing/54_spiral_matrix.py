"""
-----------------------------------------------------------------------
- Pattern: Matrix Boundary Shrinking / Simulation
- How I Recognized It: Moving along a perimeter and spiraling inwards 
  requires explicit directional loops bounded by four shrinking walls.
- Key Idea: Traverse Top -> Right -> Bottom -> Left, shifting the 
  respective boundary wall after each direction completes.
- Time Complexity: O(M * N) - Every cell is visited exactly once.
- Space Complexity: O(1) auxiliary space (excluding the output array).
-----------------------------------------------------------------------
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # 1. Move Right across the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Move Down the rightmost column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            # 3. Move Left across the bottom row (if row still exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
                
            # 4. Move Up the leftmost column (if column still exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
                
        return res