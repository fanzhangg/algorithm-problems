"""
Input: an array of numbers, a position input.
Output: The sum of values from the position to the end of the array.
"""


def sum_after(nums: list, pos=0):
    if pos < 0:
        pos = 0
    if pos > len(nums) - 1:
        return 0
    if pos == len(nums) - 1:
        return nums[pos]
    else:
        return nums[pos] + sum_after(nums, pos+1)
