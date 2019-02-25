"""
Input: an array of integers
Output: indices of two numbers such as they add up to a specific target
"""


def two_sum_0(nums, target):
    """
    Brutal force
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_1(nums, target):
    """
    One-pass hash table
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in dic:
            return [dic[num], i]
        else:
            # store the diff as the key and the index as value
            diff = target - num
            dic[diff] = i


def two_sum_2(nums, target):
    """
    One-pass hash table
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in dic:
            return [dic[diff], i]
        else:
            # store the diff as the key and the index as value
            dic[num] = i
