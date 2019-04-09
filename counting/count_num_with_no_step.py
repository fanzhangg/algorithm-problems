from itertools import permutations


def has_step(nums: tuple) -> bool:
    """
    * A step is any spot where i is immediately followed by i + 1 (i.e. 12345's step is 4, 54321's step is 0)
    :param nums: a permutation of numbers
    :return: true if the permutation has at least 1 step
    """
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            return True
    return False


def count_num_with_no_steps(nums: list)->int:
    """
    :param nums: numbers
    :return: number of permutations of nums with no steps
    """
    count = 0
    permutes = list(permutations(nums, len(nums)))
    for i in permutes:
        if not has_step(i):
            print(i)
            count += 1
    return count


if __name__ == "__main__":
    count = count_num_with_no_steps([1, 2, 3, 4, 5])
    print(count)
