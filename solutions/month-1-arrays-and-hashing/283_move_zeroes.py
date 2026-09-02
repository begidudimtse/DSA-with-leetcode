class Solution:
    def moveZeroes(nums):
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != 0:
                nums[writer] = nums[reader]
                writer += 1
# time complexity: O(n)
# space complexity: O(1)