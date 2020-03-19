def containsDuplicate(nums):
        """
        :type nums: List[int] an array of integers
        :rtype: bool True if the array contains duplicates
        """
        counter = set()

        for n in nums:
            if n in counter:
                return True
            counter.add(n)

        return False
