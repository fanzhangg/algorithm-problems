def containsNearbyDuplicate(nums, k):
        """
        Given an array of integers and an integer k, 
        find out whether there are two distinct indices i and j in the array 
        such that nums[i] = nums[j] and the absolute difference between i and j 
        is at most k.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = {}

        for idx, value in enumerate(nums):
            if value in counter and idx - counter[value] <= k:
                return True
            counter[value] = idx
        return False


print(containsNearbyDuplicate([2, 3, 4, 5, 2, 6], 2))
