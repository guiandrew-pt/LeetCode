class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position to place the next non-zero element
        non_zero_position = 0

        # Traverse the list
        for i in range(len(nums)):
            if nums[i] != 0:
                # Place the non-zero element at the non_zero_position index
                nums[non_zero_position] = nums[i]

                # If i and non_zero_position are different, set the current position to 0
                if i != non_zero_position:
                    nums[i] = 0
                non_zero_position += 1